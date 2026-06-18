local portal = _G["gg_unit_n003_0941"]
if portal==nil then return "nil portal" end
local out={}
local function L(s) out[#out+1]=s end
L("portal name="..GetUnitName(portal).." typeId set")
L("owner player="..GetPlayerId(GetOwningPlayer(portal)))
L("mana="..GetUnitState(portal,UNIT_STATE_MANA).." maxmana="..BlzGetUnitMaxMana(portal))
L("order BEFORE="..tostring(GetUnitCurrentOrder(portal)))
-- candidate web-ish ability codes
for _,a in ipairs({"web","A0FX","ANcs","Aro4"}) do end
-- try the cast both ways
local r1 = IssueImmediateOrder(portal, "web")
L("IssueImmediateOrder('web') returned="..tostring(r1))
L("order AFTER immediate="..tostring(GetUnitCurrentOrder(portal)))
local r2 = IssueImmediateOrderBJ(portal, "web")
L("IssueImmediateOrderBJ('web') called")
L("order AFTER bj="..tostring(GetUnitCurrentOrder(portal)))
-- also dump ability levels for a few likely codes
local function lvl(code) return GetUnitAbilityLevel(portal, FourCC(code)) end
L("abil web(Aweb)="..lvl("Aweb").." A0web? ")
return table.concat(out,"\n")
