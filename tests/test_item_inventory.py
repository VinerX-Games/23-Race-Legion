"""Pickup restrictions and AI purchases, including synchronous pickup rejection."""
import unittest
from pathlib import Path

from lupa.lua53 import LuaRuntime

SECTIONS = Path(__file__).resolve().parents[1] / 'map.w3x/_lua/monolith_split/sections'

FIXTURE = r'''
function FourCC(s) return s end
function GetOwningPlayer(u) return u.owner end
function GetUnitX(u) return 100 end
function GetUnitY(u) return 200 end
function GetUnitLoc(u) return {100,200} end
function RemoveLocation() end
function GetTriggerUnit() return eventUnit end
function GetManipulatedItem() return eventItem end
function GetItemTypeId(it) return it and not it.removed and it.id or 0 end
function UnitInventorySize(u) return u.size end
function UnitItemInSlot(u,s) return u.slots[s] end
function UnitItemInSlotBJ(u,s) return UnitItemInSlot(u,s-1) end
function GetForLoopIndexA() return bj_forLoopAIndex end
function UnitHasItem(u,it)
    for s=0,u.size-1 do if u.slots[s]==it then return true end end
    return false
end
function UnitInventoryCount(u)
    local count=0
    for s=0,u.size-1 do if u.slots[s] then count=count+1 end end
    return count
end
function CreateItem(id,x,y)
    if failCreate then return nil end
    local it={id=id}; items[#items+1]=it; return it
end
function RemoveItem(it)
    it.removed=true
    for _,u in ipairs(heroes) do
        for s=0,u.size-1 do if u.slots[s]==it then u.slots[s]=nil end end
    end
end
function UnitDropItemPoint(u,it,x,y)
    for s=0,u.size-1 do if u.slots[s]==it then u.slots[s]=nil end end
    drops=drops+1
    return true
end
function UnitDropItemPointLoc(u,it,loc) return UnitDropItemPoint(u,it,loc[1],loc[2]) end
function DisplayTextToPlayer() messages=messages+1 end
function UnitAddItem(u,it)
    if rejectAdd then return false end
    for s=0,u.size-1 do
        if not u.slots[s] then
            u.slots[s]=it; eventUnit=u; eventItem=it
            Trig_No2SameItems_Actions()
            if rejectPickup and UnitHasItem(u,it) then UnitDropItemPoint(u,it,100,200) end
            return true
        end
    end
    return false
end
function UnitAddItemById(u,id)
    local it=CreateItem(id,100,200)
    if it and UnitAddItem(u,it) and UnitHasItem(u,it) then return it end
    return nil
end
function CreateGroup() groups=groups+1; return {} end
function DestroyGroup() groups=groups-1 end
function GroupEnumUnitsOfPlayer(g,p,filter)
    for k in pairs(g) do g[k]=nil end
    for _,u in ipairs(heroes) do if u.owner==p then g[#g+1]=u end end
end
function GroupPickRandomUnit2(g) return g[1] end
function GetRandomInt(a,b) assert(b>=a); return randomLast and b or a end
function GetPlayerState() return gold end
function SetPlayerState(p,state,n) gold=n end
function GetUnitState(u,state) return u.mana end
PLAYER_STATE_RESOURCE_GOLD='gold'; UNIT_STATE_MAX_MANA='mana'
heroes={}; items={}; messages=0; drops=0; gold=10000; groups=0
gGroup={sentinel=true}; bj_forLoopAIndex=1
hero={owner=3,size=6,slots={},mana=100}; heroes[1]=hero
function put(s,id)
    local it=CreateItem(id,100,200); hero.slots[s]=it; return it
end
function pickup(s,id)
    eventUnit=hero; eventItem=put(s,id); Trig_No2SameItems_Actions(); return eventItem
end
function groundCount()
    local n=0
    for _,it in ipairs(items) do
        if not it.removed then
            local carried=false
            for _,u in ipairs(heroes) do if UnitHasItem(u,it) then carried=true end end
            if not carried then n=n+1 end
        end
    end
    return n
end
'''


class ItemInventoryTests(unittest.TestCase):
    def setUp(self):
        self.lua = LuaRuntime()
        self.lua.execute(FIXTURE)
        for section in ('libraries/11_LibDifferentAiStuff.lua',
                        '80_runtime/triggers/05_common_spells.lua'):
            self.lua.execute((SECTIONS / section).read_text(encoding='utf-8-sig'))

    def check(self, code):
        self.lua.execute(code)

    def test_distinct_items_allowed_in_every_slot_regardless_of_bj_index(self):
        for global_index in (0, 1, 3, 6, 24):
            for slot in range(6):
                with self.subTest(global_index=global_index, slot=slot):
                    self.check(f'''
                        hero.slots={{}}; messages=0; drops=0; bj_forLoopAIndex={global_index}
                        for s=0,5 do if s~={slot} then put(s,'gear'..s) end end
                        local it=pickup({slot},'different')
                        assert(UnitHasItem(hero,it) and messages==0 and drops==0)
                        assert(bj_forLoopAIndex=={global_index})
                    ''')

    def test_true_duplicate_rejected_and_original_preserved_for_every_slot_pair(self):
        for original in range(6):
            for picked in range(6):
                if original == picked:
                    continue
                with self.subTest(original=original, picked=picked):
                    self.check(f'''
                        hero.slots={{}}; messages=0; drops=0; bj_forLoopAIndex=24
                        local first=put({original},'I030'); local second=pickup({picked},'I030')
                        assert(UnitHasItem(hero,first) and not UnitHasItem(hero,second))
                        assert(not second.removed and messages==1 and drops==1)
                    ''')

    def test_consumables_follow_same_exact_type_rule(self):
        self.check('''
            local first=pickup(0,'phea'); local mana=pickup(1,'pman')
            local greater=pickup(2,'pghe'); local duplicate=pickup(3,'phea')
            assert(UnitHasItem(hero,first) and UnitHasItem(hero,mana) and UnitHasItem(hero,greater))
            assert(not UnitHasItem(hero,duplicate) and messages==1)
        ''')

    def test_missing_or_consumed_event_item_is_ignored(self):
        self.check('''
            eventUnit=hero; eventItem=nil; Trig_No2SameItems_Actions()
            eventItem={id='phea',removed=true}; Trig_No2SameItems_Actions()
            eventItem={id='phea'}; Trig_No2SameItems_Actions()
            assert(messages==0 and drops==0)
        ''')

    def test_repeated_ai_purchases_fill_inventory_without_duplicates_or_ground_items(self):
        for tier in (20, 50, 200):
            with self.subTest(tier=tier):
                self.setUp()
                self.check(f'''
                    for i=1,100 do TryBuy(3,{tier}) end
                    assert(UnitInventoryCount(hero)==6 and gold==5700)
                    local owned={{}}
                    for s=0,5 do local id=GetItemTypeId(hero.slots[s]); assert(not owned[id]); owned[id]=true end
                    assert(owned.phea and owned.pman and groundCount()==0 and messages==0)
                    assert(groups==0 and gGroup.sentinel)
                ''')

    def test_ai_rejected_add_or_pickup_is_cleaned_without_charging(self):
        for gear in (False, True):
            for rejection in ('rejectAdd', 'rejectPickup', 'failCreate'):
                with self.subTest(gear=gear, rejection=rejection):
                    self.setUp()
                    self.check(('put(0,"pghe"); put(1,"pgma");' if gear else '') + f'''
                        {rejection}=true
                        for i=1,100 do TryBuy(3,50) end
                        assert(gold==10000 and groundCount()==0 and groups==0)
                    ''')

    def test_ai_no_inventory_no_hero_or_insufficient_gold_does_not_spawn_items(self):
        for setup in ('hero.size=0', 'heroes={}', 'gold=149',
                      "put(0,'phea'); put(1,'pman'); gold=999"):
            with self.subTest(setup=setup):
                self.setUp()
                self.check(setup + '; local before=#items; TryBuy(3,50); assert(#items==before and groundCount()==0 and groups==0)')

    def test_ai_skips_mana_potion_for_manaless_hero(self):
        self.check('''
            hero.mana=0
            for i=1,100 do TryBuy(3,20) end
            assert(UnitInventoryCount(hero)==6 and gold==4850 and groundCount()==0)
            for s=0,5 do assert(GetItemTypeId(hero.slots[s])~='pman') end
        ''')

    def test_ai_already_owned_tier_items_are_skipped_at_both_random_boundaries(self):
        for last in (False, True):
            with self.subTest(last=last):
                self.setUp()
                self.check(f'''
                    randomLast={str(last).lower()}; bj_forLoopAIndex=24
                    put(0,'phea'); put(1,'pman'); put(2,'I02S'); put(3,'I02X')
                    TryBuy(3,20)
                    assert(UnitInventoryCount(hero)==5 and gold==9000 and groundCount()==0)
                    assert(GetItemTypeId(hero.slots[4])=='{ 'I02T' if last else 'I030' }')
                ''')


if __name__ == '__main__':
    unittest.main()
