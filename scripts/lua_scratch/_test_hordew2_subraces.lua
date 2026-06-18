-- Live-bridge snippet for a quick 3-bot HordeW2 comparison.
-- Usage:
--   python agent_bridge.py exec --file _test_hordew2_subraces.lua
-- Assumes the chosen player slots are free.

createAiPlayer(5, "hordew2base")
createAiPlayer(6, "hordew2dark")
createAiPlayer(7, "hordew2dragonmaw")

return {
    p6 = { race = AiRace[5], subrace = HordeW2GetSubrace(5) },
    p7 = { race = AiRace[6], subrace = HordeW2GetSubrace(6) },
    p8 = { race = AiRace[7], subrace = HordeW2GetSubrace(7) },
}
