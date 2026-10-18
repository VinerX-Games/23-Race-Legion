local t = DraeneiLiveTest
assert(t ~= nil, 'test setup absent')
assert(DraeneiCombat.protection[t.vowTarget] ~= nil, 'native vow cast did not grant protection')
assert(GetUnitState(t.waveTarget, UNIT_STATE_LIFE) >= 1130, 'native wave did not heal primary')
assert(GetUnitState(t.waveSecond, UNIT_STATE_LIFE) >= 1097.5, 'native wave did not bounce')
assert(DraeneiCombat.protection[t.waveTarget] ~= nil, 'wave did not grant researched blessing')
assert(GetUnitState(t.secondary, UNIT_STATE_LIFE) < 2000, 'prismatic shards did not deal damage')
local ward
for _, data in ipairs(DraeneiCombat.wards) do
    if data.caster == t.seer then ward = data.unit end
end
assert(ward ~= nil and GetUnitTypeId(ward) == FourCC('nDr1'), 'native idol cast did not summon memory idol')
return 'passed'
