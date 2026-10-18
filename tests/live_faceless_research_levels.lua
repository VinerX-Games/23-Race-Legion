-- Isolated engine observation. Temporary units and research state are restored.
local p = Player(PLAYER_NEUTRAL_PASSIVE)
local savedEs = GetPlayerTechCount(p, FourCC('R0ES'), true)
local savedGd = GetPlayerTechCount(p, FourCC('R0GD'), true)
local units = {}
local rows = {}
local function spawn(code)
    local u = CreateUnit(p, FourCC(code), 0, 0, 0)
    assert(u ~= nil, 'Could not create ' .. code)
    units[#units + 1] = u
    SetUnitInvulnerable(u, true)
    PauseUnit(u, true)
    return u
end
local ok, problem = pcall(function()
    SetPlayerTechResearched(p, FourCC('R0ES'), 0)
    local fear = spawn('h0MN')
    for level = 0, 3 do
        SetPlayerTechResearched(p, FourCC('R0ES'), level)
        local fresh = spawn('h0MN')
        rows[#rows + 1] = string.format('R0ES:%d existing=%d/%d fresh=%d/%d', level,
            GetUnitAbilityLevel(fear, FourCC('A1CK')), GetUnitAbilityLevel(fear, FourCC('A1CF')),
            GetUnitAbilityLevel(fresh, FourCC('A1CK')), GetUnitAbilityLevel(fresh, FourCC('A1CF')))
    end
    SetPlayerTechResearched(p, FourCC('R0GD'), 0)
    local caster = spawn('h0K2')
    for level = 0, 3 do
        SetPlayerTechResearched(p, FourCC('R0GD'), level)
        local fresh = spawn('h0K2')
        rows[#rows + 1] = string.format('R0GD:%d existing=%d/%.1f fresh=%d/%.1f', level,
            BlzGetUnitMaxHP(caster), GetUnitState(caster, UNIT_STATE_MAX_MANA),
            BlzGetUnitMaxHP(fresh), GetUnitState(fresh, UNIT_STATE_MAX_MANA))
    end
end)
for _, u in ipairs(units) do RemoveUnit(u) end
SetPlayerTechResearched(p, FourCC('R0ES'), savedEs)
SetPlayerTechResearched(p, FourCC('R0GD'), savedGd)
assert(ok, tostring(problem))
return table.concat(rows, '|')
