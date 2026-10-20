"""Race research and kill rewards use the units and owners from their event."""
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime


ROOT = Path(__file__).resolve().parents[1]
RACES = ROOT / 'map.w3x/_lua/monolith_split/sections/80_runtime/triggers/races'


def load_block(lua, filename, first, following):
    source = (RACES / filename).read_text(encoding='utf-8')
    block = source.split('function ' + first + '()', 1)[1]
    block = block.split('function ' + following + '()', 1)[0]
    lua.execute('function ' + first + '()' + block)


class GoblinFuelResearchTests(unittest.TestCase):
    ability = 'A0A5'
    research = 'R04N'
    research_trigger = 'Potreblenie'
    train_trigger = 'PotreblenieTrain'

    def setUp(self):
        self.lua = LuaRuntime()
        setup = '''
            research = {[2]=3, [7]=1}
            building = {owner=2, fuel=0}
            trained = {owner=2, fuel=1}
            existing = {owner=2, fuel=1}
            ordinary = {owner=2, fuel=0}
            foreign = {owner=7, fuel=1}
            units = {existing, ordinary, foreign}
            udg_LocalPlayer = 7
            udg_LocalOtrad2 = {sentinel=true}
            udg_Boolexpr = 'unchanged'
            disabled = {}
            created, destroyed = 0, 0
            function FourCC(code) return code end
            function GetTriggerUnit() return building end
            function GetTrainedUnit() return trained end
            function GetOwningPlayer(unit) assert(unit); return unit.owner end
            function GetResearched() return 'R04N' end
            function GetPlayerTechCountSimple(code, owner)
                assert(code == 'R04N'); return research[owner]
            end
            function GetUnitAbilityLevelSwapped(code, unit)
                assert(code == 'A0A5' and unit); return unit.fuel
            end
            function SetUnitAbilityLevelSwapped(code, unit, level)
                assert(code == 'A0A5' and unit and level >= 1 and level <= 6)
                unit.fuel = level
            end
            function SetPlayerAbilityAvailableBJ(available, code, owner)
                assert(available == false and code == 'A0A5')
                disabled[owner] = true
            end
            function CachedFilter(fn) return fn end
            function GetFilterUnit() return filtered end
            function GetEnumUnit() return enumerated end
            function CreateGroup() created = created + 1; return {} end
            function GroupEnumUnitsOfPlayer(group, owner, filter)
                assert(group ~= udg_LocalOtrad2)
                for _, unit in ipairs(units) do
                    filtered = unit
                    if unit.owner == owner and filter() then
                        group[#group+1] = unit
                    end
                end
                filtered = nil
            end
            function ForGroupBJ(group, action)
                for _, unit in ipairs(group) do enumerated=unit; action() end
                enumerated = nil
            end
            function DestroyGroup(group)
                assert(group ~= udg_LocalOtrad2); destroyed = destroyed + 1
            end
        '''
        self.lua.execute(setup.replace('A0A5', self.ability).replace('R04N', self.research))
        load_block(self.lua, 'Goblins.lua', f'Trig_{self.research_trigger}_Conditions',
                   f'InitTrig_{self.research_trigger}')
        load_block(self.lua, 'Goblins.lua', f'Trig_{self.train_trigger}_Conditions',
                   f'InitTrig_{self.train_trigger}')
        self.lua.execute(f'''
            Trig_Potreblenie_Actions = Trig_{self.research_trigger}_Actions
            Trig_PotreblenieTrain_Conditions = Trig_{self.train_trigger}_Conditions
            Trig_PotreblenieTrain_Actions = Trig_{self.train_trigger}_Actions
        ''')

    def test_research_updates_only_owners_mechanisms_and_releases_group(self):
        self.lua.execute('Trig_Potreblenie_Actions()')
        state = self.lua.globals()
        self.assertEqual(state.existing.fuel, 4)
        self.assertEqual(state.ordinary.fuel, 0)
        self.assertEqual(state.foreign.fuel, 1)
        self.assertEqual(state.udg_LocalPlayer, 7)
        self.assertEqual(state.udg_Boolexpr, 'unchanged')
        self.assertTrue(state.udg_LocalOtrad2.sentinel)
        self.assertEqual(state.created, 1)
        self.assertEqual(state.destroyed, 1)

    def test_trained_mechanism_receives_every_supported_research_level(self):
        for level in range(6):
            with self.subTest(level=level):
                state = self.lua.globals()
                state.research[2] = level
                self.lua.execute('''
                    trained.fuel = 1
                    Trig_Potreblenie_Actions()
                    if Trig_PotreblenieTrain_Conditions() then
                        Trig_PotreblenieTrain_Actions()
                    end
                ''')
                self.assertEqual(state.trained.fuel, level + 1)
                self.assertEqual(state.existing.fuel, state.trained.fuel)
                self.assertEqual(state.building.fuel, 0)

    def test_trained_unit_without_fuel_is_ignored(self):
        self.lua.execute('trained.fuel=0')
        self.assertFalse(self.lua.globals().Trig_PotreblenieTrain_Conditions())

    def test_training_uses_trained_unit_owner(self):
        self.lua.execute('trained.owner=7; Trig_PotreblenieTrain_Actions()')
        self.assertEqual(self.lua.globals().trained.fuel, 2)

    def test_final_research_disables_fuel_for_owner_without_level_seven(self):
        self.lua.execute('research[2]=6; Trig_Potreblenie_Actions()')
        state = self.lua.globals()
        self.assertTrue(state.disabled[2])
        self.assertIsNone(state.disabled[7])
        self.lua.execute('disabled={}; Trig_PotreblenieTrain_Actions()')
        self.assertTrue(state.disabled[2])
        self.assertIsNone(state.disabled[7])


class GoblinDefectiveAmmoTests(GoblinFuelResearchTests):
    ability = 'A0A6'
    research = 'R05W'
    research_trigger = 'BracResearch'
    train_trigger = 'BracTrain'


class GoblinSelfIgnitionTests(GoblinFuelResearchTests):
    ability = 'A0AR'
    research = 'R04R'
    research_trigger = 'PodjogResearch'
    train_trigger = 'PodjogTrain'


class GoblinSelfExplosionTests(GoblinFuelResearchTests):
    ability = 'A0A9'
    research = 'R04Q'
    research_trigger = 'PodruvResearc'
    train_trigger = 'PodruvTrain'


class W2VeteranDamageTests(unittest.TestCase):
    def test_additional_damage_is_one_percent_per_rank_and_triggers_restore(self):
        lua = LuaRuntime()
        lua.execute('''
            ATTACK_TYPE_NORMAL, DAMAGE_TYPE_UNIVERSAL = 'normal', 'universal'
            gg_trg_DamageBeforeW2, gg_trg_DamagerW2 = 'bonus', 'xp'
            attacker, target = {}, {}
            UHData = {[1]={lvl=0}}
            enabled = {bonus=true, xp=true}
            function GetEventDamageSource() return attacker end
            function GetTriggerUnit() return target end
            function GetHandleId(u) assert(u==attacker); return 1 end
            function GetEventDamage() return 100 end
            function DisableTrigger(t) enabled[t]=false end
            function EnableTrigger(t) enabled[t]=true end
            function UnitDamageTargetBJ(source, victim, damage, attack, kind)
                assert(source==attacker and victim==target)
                assert(attack=='normal' and kind=='universal')
                assert(not enabled.bonus and not enabled.xp)
                bonusDamage = damage
            end
        ''')
        load_block(lua, 'HordeW2.lua', 'Trig_DamageBeforeW2_Actions',
                   'InitTrig_DamageBeforeW2')
        for rank in (0, 1, 5, 8, 10):
            with self.subTest(rank=rank):
                lua.globals().UHData[1].lvl = rank
                lua.globals().Trig_DamageBeforeW2_Actions()
                self.assertAlmostEqual(lua.globals().bonusDamage, rank)
                self.assertTrue(lua.globals().enabled.bonus)
                self.assertTrue(lua.globals().enabled.xp)


class RaceKillRewardTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime()
        self.lua.execute('''
            UNIT_TYPE_SUMMONED = 'summoned'
            killer = {owner=2, abilities={A1R3=1, A1R5=0, w2a0=1}}
            victim = {owner=7, allied=false, summoned=false}
            xp, bonuses, removals = 0, 0, 0
            function FourCC(code) return code end
            function GetKillingUnit() return killer end
            function GetTriggerUnit() return victim end
            function GetOwningPlayer(unit) assert(unit); return unit.owner end
            function GetUnitAbilityLevel(unit, code)
                return unit and unit.abilities[code] or 0
            end
            function GetEventDamageSource()
                error('Damage source is not a response to a death event')
            end
            function IsUnitEnemy(unit, owner)
                return unit.owner ~= owner and not unit.allied
            end
            function IsUnitType(unit, kind)
                assert(kind == UNIT_TYPE_SUMMONED); return unit.summoned
            end
            function AddXp(unit, amount)
                assert(unit == killer and amount == 55); xp = xp + amount
            end
            function UnitAddAbility(unit, code)
                assert(unit == killer and code == 'A1R5')
                unit.abilities[code] = 1; bonuses = bonuses + 1
            end
            function RemoveAbilityTimed(unit, code, duration)
                assert(unit == killer and code == 'A1R5' and duration == 9)
                removals = removals + 1
            end
        ''')
        load_block(self.lua, 'Stromgard.lua', 'Trig_ChillBonus_Conditions',
                   'InitTrig_ChillBonus')
        load_block(self.lua, 'HordeW2.lua', 'Trig_KillW2_Conditions',
                   'InitTrig_KillW2')

    def kill(self, trigger):
        self.lua.execute(f'if Trig_{trigger}_Conditions() then Trig_{trigger}_Actions() end')

    def test_devouring_enemy_grants_one_bonus_without_refresh(self):
        self.kill('ChillBonus')
        self.kill('ChillBonus')
        self.assertEqual(self.lua.globals().bonuses, 1)
        self.assertEqual(self.lua.globals().removals, 1)

    def test_devouring_summoned_enemy_grants_no_bonus(self):
        self.lua.execute('victim.summoned=true')
        self.kill('ChillBonus')
        self.assertEqual(self.lua.globals().bonuses, 0)

    def test_allied_and_owned_victims_grant_neither_reward(self):
        for setup in ('victim.allied=true', 'victim.allied=false; victim.owner=2'):
            with self.subTest(setup=setup):
                self.lua.execute(setup)
                self.kill('ChillBonus')
                self.kill('KillW2')
                self.assertEqual(self.lua.globals().bonuses, 0)
                self.assertEqual(self.lua.globals().xp, 0)

    def test_missing_killer_or_ability_grants_neither_reward(self):
        for setup in ('killer.abilities={}', 'killer=nil'):
            with self.subTest(setup=setup):
                self.lua.execute(setup)
                self.kill('ChillBonus')
                self.kill('KillW2')
                self.assertEqual(self.lua.globals().bonuses, 0)
                self.assertEqual(self.lua.globals().xp, 0)

    def test_w2_enemy_kill_grants_55_xp_without_damage_event(self):
        self.kill('KillW2')
        self.assertEqual(self.lua.globals().xp, 55)


if __name__ == '__main__':
    unittest.main()
