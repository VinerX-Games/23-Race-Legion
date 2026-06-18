-- Diagnose player 5: army-size vs limit, and why portal isn't applied.
local pi = 5
local p = Player(pi)
local out = {}
local function L(s) out[#out+1] = s end

L("=== P"..pi.." race="..tostring(AiRace and AiRace[pi]).." fsm="..tostring(AiSquadFsmEnabled))
L("globals: AiSizeScale="..tostring(AiSizeScale).." AiBrainDesiredArmy="..tostring(AiBrainDesiredArmy)
  .." AiSquadMaxCount="..tostring(AiSquadMaxCount).." AiSquadTargetSize="..tostring(AiSquadTargetSize))

local race = AiRaceOf and AiRaceOf(pi)
if race then
  local desiredRaw = race.desiredArmy or AiBrainDesiredArmy
  local desired = AiScaled and AiScaled(desiredRaw) or desiredRaw
  L("desiredRaw="..tostring(desiredRaw).." -> AiScaled desired="..tostring(desired))
end

-- live army count
local army = udg_Ai_army and udg_Ai_army[pi]
local armyCnt, alive = 0, 0
if army then
  local sz = BlzGroupGetSize(army)
  armyCnt = sz
  for i=0,sz-1 do
    local u = BlzGroupUnitAt(army,i)
    if u and GetUnitState(u,UNIT_STATE_LIFE)>0.405
       and not IsUnitType(u,UNIT_TYPE_PEON)
       and not IsUnitType(u,UNIT_TYPE_STRUCTURE) then alive=alive+1 end
  end
end
L("army group size="..armyCnt.." alive-mil="..alive)

-- squads
local squads = AiSquadsOf and AiSquadsOf(pi) or {}
local assault, defense, total = 0,0,0
for sid,sq in pairs(squads) do
  total = total+1
  local sz = sq.members and BlzGroupGetSize(sq.members) or 0
  if sq.role=="assault" then assault=assault+1 end
  if sq.role=="defense" then defense=defense+1 end
  L("  squad "..tostring(sid).." role="..tostring(sq.role).." state="..tostring(sq.state).." size="..sz)
end
L("squad totals: assault="..assault.." defense="..defense.." total="..total.." (cap AiSquadMaxCount="..tostring(AiSquadMaxCount)..")")

-- capital + continent
local wm = AiBrainPerceive and AiBrainPerceive(pi)
if wm then
  local sc = (wm.cx and AiContinentOf) and AiContinentOf(wm.cx, wm.cy) or nil
  L("capital ("..tostring(wm.cx and R2I(wm.cx))..","..tostring(wm.cy and R2I(wm.cy))..") continent="..tostring(sc)
    .." defendHome="..tostring(wm.defendHome))
  -- focus / objective
  local focus = AiBrainPickFocus and AiBrainPickFocus(pi, wm)
  if focus then
    local oc = AiContinentOf(focus.x, focus.y)
    L("focus ("..R2I(focus.x)..","..R2I(focus.y)..") continent="..tostring(oc))
    if sc and oc and sc~=oc then
      local rt = AiPortalRoute and AiPortalRoute(sc, oc)
      L("AiPortalRoute("..sc.." -> "..oc..") = "..(rt and ("["..table.concat(rt,",").."] hops="..#rt) or "nil"))
      if rt and #rt>=2 then
        local portal = AiFindPortal(rt[1], rt[2])
        if portal then
          L("AiFindPortal("..rt[1].."->"..rt[2]..") = "..GetUnitName(portal)
            .." at ("..R2I(GetUnitX(portal))..","..R2I(GetUnitY(portal))..") active="..tostring(WaygateIsActive(portal)))
        else
          L("AiFindPortal("..rt[1].."->"..rt[2]..") = nil  <-- NO PORTAL UNIT")
        end
      end
    else
      L("focus continent == capital continent (or nil) -> no portal needed")
    end
  else
    L("AiBrainPickFocus = nil (no focus)")
  end
end

return table.concat(out, "\n")
