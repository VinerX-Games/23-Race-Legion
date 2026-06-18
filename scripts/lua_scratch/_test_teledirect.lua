local pi = 5
local portal = _G["gg_unit_n003_0941"]
local rect   = _G["gg_rct_DarkM_2"]
if portal==nil or rect==nil then return "nil portal="..tostring(portal==nil).." rect="..tostring(rect==nil) end

local army = udg_Ai_army[pi]
local sz = BlzGroupGetSize(army)
local function snap()
  local bc={}
  for i=0,sz-1 do
    local u=BlzGroupUnitAt(army,i)
    if u and GetUnitState(u,UNIT_STATE_LIFE)>0.405
       and not IsUnitType(u,UNIT_TYPE_PEON) and not IsUnitType(u,UNIT_TYPE_STRUCTURE) then
      local c=AiContinentOf(GetUnitX(u),GetUnitY(u)) or "nil"; bc[c]=(bc[c] or 0)+1
    end
  end
  local t={}; for c,n in pairs(bc) do t[#t+1]=c.."="..n end; return table.concat(t,", ")
end
local before = snap()
TeleportUnits(portal, rect, 1200)
local after = snap()
return "BEFORE: "..before.."\nAFTER : "..after
