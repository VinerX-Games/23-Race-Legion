-- Disable every periodic / high-frequency AI trigger so nothing iterates the ~2500 units
-- while the host hand-builds shipyards. Reversible: _ai_resume.lua re-enables them.
local trigs = {
    gg_trg_PereborPlayersForBuilders, gg_trg_PereborBuilders_Uni,
    gg_trg_PereborPlayerForArmy, gg_trg_PerebobArmy_Uni,
    gg_trg_PereborPlayerForNavy, gg_trg_PerebobNavy,
    gg_trg_PereborBuildings, gg_trg_PereborNavalBases,
    gg_trg_Strateg, gg_trg_AttackerAi, gg_trg_AttackedAI,
}
local n = 0
for _, t in ipairs(trigs) do
    if t ~= nil then DisableTrigger(t); n = n + 1 end
end
return "disabled " .. tostring(n) .. " periodic/combat AI triggers"
