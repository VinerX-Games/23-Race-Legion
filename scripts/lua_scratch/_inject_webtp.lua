-- Hot-load the new web-portal mass-TP functions into the running game and drive them.
AiWebPortalSpecs = {
  {"n003_0044","UndecityOutTop",800},{"n003_0046","UndecityOutBot",800},{"n003_0050","UndercityInR",800},
  {"n003_0051","UndercityInTop",800},{"n003_0516","OrgrimmarTopIn",800},{"n003_0514","OrgrimmarBotIn",800},
  {"n003_0517","OrgrimmarTopOut",800},{"n003_0518","OrgrimmarBotOut",800},{"n003_0521","DeadminersOut",800},
  {"n003_0420","DeadminerIn",800},{"n003_0943","DarkM_4",1200},{"n003_0942","DarkM_3",1200},
  {"n003_0940","DarkM_1",1200},{"n003_0941","DarkM_2",1200},{"n01Y_0889","ED_1",750},
  {"n01Y_1012","ED_1_B",750},{"n01Y_0934","ED_2",750},{"n01Y_1013","ED_2_b",750},
  {"n01Y_0896","ED_3",750},{"n01Y_1014","ED_3_b",750},{"n01Y_1015","ED_4_b",750},
  {"n01Y_0897","ED_4",750},{"n01Z_1016","ED_5",750},{"n01Z_1017","ED_5_B",750},
  {"n006_0023","DarkPortal1",1200},{"n006_0438","DarkPortal2",1200},{"n001_0845","Region_009",1200},
  {"n04O_0136","Region_010",1200},{"n00W_0442","EKportalAlterac",1200},{"n00W_0589","OutlandNagrand",1200},
  {"n00W_0446","Region_013",1200},{"n001_0847","Region_014",1200},{"n065_0125","ArgusShip",1200},
  {"n00W_0848","Broken_Island",1200},{"n01B_0849","Region_017",1200},{"n01B_0850","Region_018",1200},
  {"n003_0098","Nord_5",1200},{"n003_0060","AzNer_5",650},{"n003_0097","AzNer_2",1200},
  {"n003_1004","Nord4",1200},{"n003_1002","Nord_1",1200},{"n003_0995","AzNer1",1200},
  {"n01Y_0578","Teldrasil",1200},{"n01Y_0580","Darnas",1200},{"n003_0118","QtunIn",1200},
  {"n003_0117","QtunIn2",1200},{"n003_0124","QtunOut",1200},{"n003_0123","QtunOu2",1200},
  {"n003_0308","MarodonOut",900},{"n003_0311","MarodonOut2",900},{"n003_0305","MarodonIn",900},
  {"n003_0314","MarodonIn2",900},{"n003_0025","GnomreganIn",1200},{"n003_0018","GnomreganOut",1200},
  {"n003_0024","Stalgorn",1200},{"n003_0019","StalgornOut",1200},{"n003_0028","TrainIn",1200},
  {"n003_0149","TrainOut",1200},{"n003_0021","GrimBatolOut",1200},{"n003_0022","GrimBatolIn",1200},
  {"n003_0027","UldamanIn",1200},{"n003_0020","UldamanOut",1200},{"n003_0126","NaxOut",1200},
  {"n003_0588","DalaranOut",1200},{"n060_0350","Silvermoon",1200},{"n060_0287","QuelIsland",1200},
  {"n003_0090","TurtleOut",800},
}
AiWebPortals = nil
AiWebPortalCast = {}
function AiBuildWebPortalCache()
  if AiWebPortals ~= nil then return end
  AiWebPortals = {}
  for _, spec in ipairs(AiWebPortalSpecs) do
    local u = _G["gg_unit_"..spec[1]]; local r = _G["gg_rct_"..spec[2]]
    if u ~= nil and r ~= nil then
      local px,py = GetUnitX(u), GetUnitY(u)
      local sc = AiContinentOf(px,py); local dc = AiContinentOf(GetRectCenterX(r),GetRectCenterY(r))
      if sc~=nil and dc~=nil and sc~=dc then
        AiWebPortals[#AiWebPortals+1] = {unit=u,rect=r,x=px,y=py,radius=spec[3],srcCont=sc,dstCont=dc}
      end
    end
  end
end
function AiFindWebPortal(srcCont, dstCont, x, y)
  AiBuildWebPortalCache()
  local best,bestd
  for _,wp in ipairs(AiWebPortals) do
    if wp.srcCont==srcCont and wp.dstCont==dstCont and GetUnitState(wp.unit,UNIT_STATE_LIFE)>0.405 then
      local dx,dy=x-wp.x,y-wp.y; local d=dx*dx+dy*dy
      if bestd==nil or d<bestd then best,bestd=wp,d end
    end
  end
  return best
end
function AiPortalTeleport(pi, portal, rect, radius)
  local army = udg_Ai_army and udg_Ai_army[pi]; if army==nil then return 0 end
  local px,py = GetUnitX(portal),GetUnitY(portal)
  local minx,maxx=GetRectMinX(rect),GetRectMaxX(rect); local miny,maxy=GetRectMinY(rect),GetRectMaxY(rect)
  local r2=radius*radius; local moved=0; local sz=BlzGroupGetSize(army); local i=0
  while i<sz and moved<150 do
    local u=BlzGroupUnitAt(army,i); i=i+1
    if u and GetUnitState(u,UNIT_STATE_LIFE)>0.405 and not IsUnitType(u,UNIT_TYPE_STRUCTURE)
       and not IsUnitType(u,UNIT_TYPE_PEON) and GetUnitAbilityLevel(u,FourCC('Awrp'))==0 then
      local dx,dy=GetUnitX(u)-px,GetUnitY(u)-py
      if dx*dx+dy*dy<=r2 then SetUnitPosition(u,GetRandomReal(minx,maxx),GetRandomReal(miny,maxy)); moved=moved+1 end
    end
  end
  return moved
end
AiWebMinArmy=16; AiWebGatherFrac=0.40; AiWebMinGathered=10; AiWebCooldownTicks=16
function BrainWebPortalTick(pi,p,wm)
  if wm==nil or wm.defendHome then return "p"..pi..":defendHome/nil" end
  local army=udg_Ai_army[pi]; if army==nil then return "p"..pi..":noarmy" end
  local sz=BlzGroupGetSize(army); local sumx,sumy,mil=0,0,0
  for i=0,sz-1 do local u=BlzGroupUnitAt(army,i)
    if u and GetUnitState(u,UNIT_STATE_LIFE)>0.405 and not IsUnitType(u,UNIT_TYPE_STRUCTURE) and not IsUnitType(u,UNIT_TYPE_PEON) then
      sumx=sumx+GetUnitX(u);sumy=sumy+GetUnitY(u);mil=mil+1 end end
  if mil<AiWebMinArmy then return "p"..pi..":army "..mil.."<min" end
  local cx,cy=sumx/mil,sumy/mil; local ac=AiContinentOf(cx,cy); if ac==nil then return "p"..pi..":ac nil" end
  local focus=AiBrainPickFocus(pi,wm); if focus==nil then return "p"..pi..":nofocus" end
  local oc=AiContinentOf(focus.x,focus.y); if oc==nil or oc==ac then return "p"..pi..":obj="..tostring(oc).." ac="..ac.." (same/nil)" end
  local rt=AiPortalRoute(ac,oc); local nextCont=(rt and #rt>=2) and rt[2] or oc
  local wp=AiFindWebPortal(ac,nextCont,cx,cy); if wp==nil then return "p"..pi..":no webportal "..ac.."->"..tostring(nextCont) end
  local need=math.max(AiWebMinGathered,math.ceil(mil*AiWebGatherFrac))
  local within,r2=0,wp.radius*wp.radius
  for i=0,sz-1 do local u=BlzGroupUnitAt(army,i)
    if u and GetUnitState(u,UNIT_STATE_LIFE)>0.405 and not IsUnitType(u,UNIT_TYPE_STRUCTURE) and not IsUnitType(u,UNIT_TYPE_PEON) then
      local dx,dy=GetUnitX(u)-wp.x,GetUnitY(u)-wp.y; if dx*dx+dy*dy<=r2 then within=within+1 end end end
  if within<need then return "p"..pi..":gathering "..within.."/"..need.." @"..ac.."->"..wp.dstCont end
  local moved=AiPortalTeleport(pi,wp.unit,wp.rect,wp.radius)
  AiWebPortalCast[tostring(wp.unit)]=0
  return "p"..pi..":MASS-TP moved="..moved.." "..ac.."->"..wp.dstCont.." (obj "..oc..")"
end

-- drive across all 16 bots
local res={}
for pi=1,16 do
  if AiBrainEnabled and AiBrainEnabled(pi) then
    local ok,r = pcall(function() return BrainWebPortalTick(pi, Player(pi), AiBrainPerceive(pi)) end)
    res[#res+1]= ok and r or ("p"..pi..":ERR "..tostring(r))
  end
end
return table.concat(res,"\n")
