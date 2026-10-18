assert(type(DraeneiCombat) == 'table' and DraeneiCombat.damageTrigger ~= nil, 'Draenei triggers not initialized')
assert(AiRace[22] == nil and AiRace[23] == nil, 'test slots occupied by AI')
DraeneiLiveTest = {units = {}, player = Player(23), enemy = Player(22)}
local t = DraeneiLiveTest
function t.Create(id, owner, x, y, hp)
    local u = CreateUnit(owner, FourCC(id), x, y, 0)
    assert(u ~= nil and GetUnitTypeId(u) == FourCC(id), 'cannot create '..id)
    t.units[#t.units + 1] = u
    BlzSetUnitMaxHP(u, 2000)
    BlzSetUnitArmor(u, 0)
    SetUnitState(u, UNIT_STATE_LIFE, hp or 2000)
    BlzSetUnitMaxMana(u, 1000)
    SetUnitState(u, UNIT_STATE_MANA, 1000)
    return u
end
for _, id in ipairs({'RDr1','RDr2','RDr3','RDr4','RDr5'}) do
    SetPlayerTechResearched(t.player, FourCC(id), 1)
end
t.ranger = t.Create('e000', t.player, 24000, 24000)
t.sword = t.Create('h059', t.player, 24000, 24100)
t.enemyUnit = t.Create('hfoo', t.enemy, 24100, 24000)
t.secondary = t.Create('hfoo', t.enemy, 24150, 24000)
assert(GetUnitAbilityLevel(t.ranger, FourCC('ADr1')) > 0, 'prismatic ability missing')
assert(GetUnitAbilityLevel(t.ranger, FourCC('A05U')) == 0, 'old arrows still equipped')
assert(GetUnitAbilityLevel(t.sword, FourCC('ADr2')) > 0, 'blade ability missing')
assert(GetUnitAbilityLevel(t.sword, FourCC('A05S')) == 0, 'old critical still equipped')
UnitDamageTarget(t.ranger, t.enemyUnit, 20, true, false, ATTACK_TYPE_CHAOS, DAMAGE_TYPE_UNIVERSAL, WEAPON_TYPE_WHOKNOWS)
assert(DraeneiCombat.units[t.ranger] ~= nil and DraeneiCombat.units[t.ranger].charges == 1, 'native attack did not consume prismatic charge')
UnitDamageTarget(t.sword, t.enemyUnit, 20, true, false, ATTACK_TYPE_CHAOS, DAMAGE_TYPE_UNIVERSAL, WEAPON_TYPE_WHOKNOWS)
assert(DraeneiCombat.units[t.sword] ~= nil and DraeneiCombat.units[t.sword].bladeRemaining > 0, 'native attack did not activate blade')
t.paladin = t.Create('h01O', t.player, 24000, 22000)
t.vowTarget = t.Create('hfoo', t.player, 24100, 22000)
t.hero = t.Create('Hpal', t.player, 24200, 22000)
DraeneiCombat.ApplyVow(t.paladin, t.hero)
assert(DraeneiCombat.protection[t.hero].vowReduction == 0.15 and DraeneiCombat.protection[t.hero].vowCharges == 2, 'hero vow not weakened')
assert(IssueTargetOrder(t.paladin, 'spiritlink', t.vowTarget), 'vow order rejected')
t.priest = t.Create('h01R', t.player, 22000, 24000)
t.waveTarget = t.Create('hfoo', t.player, 22100, 24000, 1000)
t.waveSecond = t.Create('hfoo', t.player, 22200, 24000, 1000)
assert(IssueTargetOrder(t.priest, 'healingwave', t.waveTarget), 'wave order rejected')
t.seer = t.Create('n005', t.player, 22000, 22000)
assert(IssuePointOrder(t.seer, 'healingward', 22100, 22000), 'idol order rejected')
return 'created'
