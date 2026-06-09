
-- ***************************************************************************
-- *  TimedUpdate
---@param u unit
---@param p player
---@return nothing
function TimedUpdate(u, p)
    local currentLevel = 1
    local pi = GetPlayerId(p)
    
    UnitAddAbility(u, FourCC('A10G'))
    BlzStartUnitAbilityCooldown(u, FourCC('A10G'), 300)
    
    local function tick(tt)
        local levels = 4
        if GetUnitAbilityLevel(GetTriggerUnit(), FourCC('A1N9')) > 0 then
            levels = levels - 2
        end
        
        if GetOwningPlayer(u) == p and UnitAlive(u) and currentLevel <= levels then
            BlzStartUnitAbilityCooldown(u, FourCC('A10G'), 300)
            
            if GetUnitAbilityLevel(u, FourCC('A0AY')) == 0 then
                UnitAddAbility(u, FourCC('A0AY'))
                income[pi] = income[pi] + 100
            elseif GetUnitAbilityLevel(u, FourCC('A0AY')) < levels then
                income[pi] = income[pi] + 100
                IncUnitAbilityLevel(u, FourCC('A0AY'))
            else
                income[pi] = income[pi] + 100
                UnitRemoveAbility(u, FourCC('A0AZ'))
            end
            
            if GetUnitAbilityLevel(u, FourCC('A0B5')) == 0 then
                UnitAddAbility(u, FourCC('A0B5'))
                incomeW[pi] = incomeW[pi] + 50.00
            elseif GetUnitAbilityLevel(u, FourCC('A0B5')) < levels then
                IncUnitAbilityLevel(u, FourCC('A0B5'))
                incomeW[pi] = incomeW[pi] + 50.00
            else
                UnitRemoveAbility(u, FourCC('A0B1'))
            end
            
            if GetUnitAbilityLevel(u, FourCC('A0AY')) + GetUnitAbilityLevel(u, FourCC('A0B5')) >= levels * 2 then
                BlzUnitHideAbility(u, FourCC('A10G'), true)
                BlzUnitDisableAbility(u, FourCC('A10G'), true, true)
            end
            
            UpdateGraf(pi)
            currentLevel = currentLevel + 1
            TimerStart(tt, 300, false, function() tick(tt) end)
        else
            DestroyTimer(tt)
        end
    end
    
    local t = CreateTimer()
    TimerStart(t, 300, false, function() tick(t) end)
end