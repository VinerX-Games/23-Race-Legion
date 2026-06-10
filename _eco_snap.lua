local o={}
for _,pi in ipairs({8,9,11,12,16,19,22}) do
  if AiRace[pi] then
    local army=udg_Ai_army[pi] and BlzGroupGetSize(udg_Ai_army[pi]) or -1
    local g=GetPlayerState(Player(pi),PLAYER_STATE_RESOURCE_GOLD)
    local l=GetPlayerState(Player(pi),PLAYER_STATE_RESOURCE_LUMBER)
    local fc=GetPlayerState(Player(pi),PLAYER_STATE_RESOURCE_FOOD_CAP)
    local bt=udg_Ai_buildersT[pi] and BlzGroupGetSize(udg_Ai_buildersT[pi]) or -1
    local h=udg_Ai_harvest[pi] and BlzGroupGetSize(udg_Ai_harvest[pi]) or -1
    local gg=udg_Ai_units[pi]; local sz=BlzGroupGetSize(gg); local bld=0
    for i=0,sz-1 do local u=BlzGroupUnitAt(gg,i); if u and GetUnitState(u,UNIT_STATE_LIFE)>0.405 and IsUnitType(u,UNIT_TYPE_STRUCTURE) then bld=bld+1 end end
    o[#o+1]=string.format("%d %s army=%d bld=%d food=%d g=%d l=%d bT=%d h=%d",pi,AiRace[pi],army,bld,fc,g,l,bt,h)
  end
end
return table.concat(o,"\n")
