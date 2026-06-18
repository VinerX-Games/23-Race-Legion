-- Find any bot whose army is inside Ankirag (Qtun dungeon) and check if it can route out.
local out={}
local function L(s) out[#out+1]=s end
for pi=1,16 do
  if AiBrainEnabled and AiBrainEnabled(pi) then
    local army=udg_Ai_army[pi]
    if army~=nil then
      local sz=BlzGroupGetSize(army)
      local bc={}
      for i=0,sz-1 do local u=BlzGroupUnitAt(army,i)
        if u and GetUnitState(u,UNIT_STATE_LIFE)>0.405 and not IsUnitType(u,UNIT_TYPE_STRUCTURE) and not IsUnitType(u,UNIT_TYPE_PEON) then
          local c=AiContinentOf(GetUnitX(u),GetUnitY(u)) or "nil"; bc[c]=(bc[c] or 0)+1 end end
      local ank=bc["Ankirag"] or 0
      if ank>0 then
        local t={}; for c,n in pairs(bc) do t[#t+1]=c.."="..n end
        L("=== P"..pi.." has "..ank.." units in Ankirag | dist: "..table.concat(t,", "))
        -- objective
        local wm=AiBrainPerceive(pi)
        local focus=AiBrainPickFocus(pi,wm)
        local oc = focus and (AiContinentOf(focus.x,focus.y) or "nil") or "nofocus"
        L("    objective continent = "..tostring(oc))
        -- waygate route + portal from Ankirag
        local rt=AiPortalRoute("Ankirag", oc)
        if rt then local s={}; for _,v in ipairs(rt) do s[#s+1]=v end; L("    AiPortalRoute(Ankirag->"..oc..") = "..table.concat(s," > "))
        else L("    AiPortalRoute(Ankirag->"..oc..") = NIL  (no waygate path out!)") end
        local rt2=AiPortalRoute("Ankirag","Kalimdor")
        L("    AiPortalRoute(Ankirag->Kalimdor) = "..(rt2 and "exists" or "NIL"))
        local fp=AiFindPortal("Ankirag","Kalimdor")
        L("    AiFindPortal(Ankirag->Kalimdor) = "..(fp and (GetUnitName(fp).." @"..R2I(GetUnitX(fp))..","..R2I(GetUnitY(fp))) or "NIL"))
      end
    end
  end
end
if #out==0 then L("no bot army currently in Ankirag") end
-- also: is Ankirag a node in the waygate graph at all?
L("AiPortalGraph has Ankirag node = "..tostring(AiPortalGraph and AiPortalGraph["Ankirag"]~=nil))
return table.concat(out,"\n")
