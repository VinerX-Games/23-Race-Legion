local pi = 5
local portal = _G["gg_unit_n003_0941"]
local rect   = _G["gg_rct_DarkM_2"]
local radius = 1200
local px,py = GetUnitX(portal), GetUnitY(portal)

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

-- teleport only THIS bot's eligible units within radius of the portal
local minx,maxx = GetRectMinX(rect), GetRectMaxX(rect)
local miny,maxy = GetRectMinY(rect), GetRectMaxY(rect)
local moved = 0
local i = 0
while i < sz do
  local u = BlzGroupUnitAt(army,i); i=i+1
  if u and GetUnitState(u,UNIT_STATE_LIFE)>0.405
     and not IsUnitType(u,UNIT_TYPE_STRUCTURE)
     and GetUnitAbilityLevel(u,FourCC('Awrp'))==0 then
    local dx,dy = GetUnitX(u)-px, GetUnitY(u)-py
    if dx*dx+dy*dy <= radius*radius then
      SetUnitPosition(u, GetRandomReal(minx,maxx), GetRandomReal(miny,maxy))
      moved = moved + 1
    end
  end
end
local after = snap()
return "moved="..moved.."\nBEFORE: "..before.."\nAFTER : "..after
