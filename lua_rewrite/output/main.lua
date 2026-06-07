-- ============================================================
-- 23 Race Legion - Lua Rewrite
-- output/main.lua — Main entry point
-- ============================================================

-- ============================================================
-- Module loading order (dependency-aware)
-- ============================================================

local modules = {
    "globals",
    "tables",
    "utils",
    "init",
    "economy",
    "stolica",
    "ai_filters",
    "ai_utils",
    "spells_common",
    "race_init",
    "spells_races_1",
    "spells_races_2",
    "lobby",
}

-- ============================================================
-- Main Initialization
-- ============================================================

function main()
    -- Map bounds (60k x 60k map)
    SetCameraBounds(
        -30720.0 + GetCameraMargin(CAMERA_MARGIN_LEFT),
        -30720.0 + GetCameraMargin(CAMERA_MARGIN_BOTTOM),
        30720.0 - GetCameraMargin(CAMERA_MARGIN_RIGHT),
        30720.0 - GetCameraMargin(CAMERA_MARGIN_TOP),
        -30720.0 + GetCameraMargin(CAMERA_MARGIN_LEFT),
        30720.0 - GetCameraMargin(CAMERA_MARGIN_TOP),
        30720.0 - GetCameraMargin(CAMERA_MARGIN_RIGHT),
        -30720.0 + GetCameraMargin(CAMERA_MARGIN_BOTTOM)
    )

    -- Environment
    SetDayNightModels("Environment\\DNC\\DNCLordaeron\\DNCLordaeronTerrain\\DNCLordaeronTerrain.mdl",
                       "Environment\\DNC\\DNCLordaeron\\DNCLordaeronUnit\\DNCLordaeronUnit.mdl")
    SetTerrainFogEx(0, 4000.0, 8000.0, 0.500, 0.706, 1.000, 1.000)
    SetWaterBaseColor(190, 190, 160, 255)
    NewSoundEnvironment("Default")
    SetAmbientDaySound("VillageDay")
    SetAmbientNightSound("VillageNight")
    SetMapMusic("Music", true, 0)

    -- Standard initialization
    InitSounds()
    CreateRegions()
    CreateCameras()
    CreateAllUnits()
    InitBlizzard()

    -- JassHelper struct init (no-op in Lua, kept for compatibility)
    jasshelper__initstructs100223406()

    -- Library initializers
    Global___Init()
    SpellSleepAOE___onInit()
    SanctifiedEnchantment___Init()

    -- Boolexpr filters and UI setup
    initBoolExprs___Init()
    UISetup()
    Face2()
    SetContinetsBooleprs()

    -- Init globals and triggers
    InitGlobals()
    InitCustomTriggers()
    RunInitializationTriggers()
end

-- ============================================================
-- RunInitializationTriggers: Execution order from vJASS
-- ============================================================

function RunInitializationTriggers()
    -- 1. Unit Indexer
    InitializeUnitIndexer()

    -- 2. Economics init (created boolexprs for income)
    InitForEconomics()

    -- 3. City control point enforcement (fix any existing cities)
    TriggerExecute(G.gg_trg_UnitUpgraded)

    -- 4. Multiboard setup
    TriggerExecute(G.gg_trg_MainInfo)

    -- 5. Initial_things: all players, income start, things init, start locations, speed fastest
    AllPlayersStart()
    StartInc()
    InitThings()
    SetStartLocations()
    SetGameSpeed(FORCE_ALL_PLAYERS, MAP_SPEED_FASTEST)

    -- 6. Transport system init
    TriggerExecute(G.gg_trg_Init)

    -- 7. Lumber tracking init
    TriggerExecute(G.gg_trg_LumberTest)

    -- 8. FelGolem special trigger
    TriggerExecute(G.gg_trg_FelGolemStrike)

    -- 9. Second globals pass
    TriggerExecute(G.gg_trg_InitGlobals)

    -- 10. Kill test units (cleanup)
    TriggerExecute(G.gg_trg_KillTestUnits___OFF_ME)

    -- 11. AI army enumeration
    TriggerExecute(G.gg_trg_PereborPlayerForArmy)

    -- 12. AI navy enumeration
    TriggerExecute(G.gg_trg_PereborPlayerForNavy)

    -- 13. Portal fix pass
    TriggerExecute(G.gg_trg_PortalFix)

    -- 14-16. Moving cities ownership
    TriggerExecute(G.gg_trg_Owner)
    TriggerExecute(G.gg_trg_OwnerNax)
    TriggerExecute(G.gg_trg_OwnerTurtle)
end

-- ============================================================
-- InitCustomTriggers: All standard InitTrig calls
-- ============================================================
-- In the original vJASS, this calls ~1294 InitTrig_X functions.
-- In Lua, we map them to our converted functions.

function InitCustomTriggers()
    InitEconomyTriggers()
    InitSpellsRaces2()

    -- Race init triggers are in race_init.lua
    InitTrig_Race_Bezlikie_O()
    InitTrig_Race_IceTrols_O()
    InitTrig_Race_Stromgard_O()
    InitTrig_Race_Dragon_O()
    InitTrig_Race_Dragon2_O()
    InitTrig_Race_Argvinol_O()
    InitTrig_Race_Elements_O()
    InitTrig_Race_Goblins_O()
    InitTrig_Race_Demon_O()
    InitTrig_Race_Illidari_O()
    InitTrig_Race_Bandits_O()
    InitTrig_Race_RedOrden_O()
    InitTrig_Race_Undead_O()
    InitTrig_Race_Horde_O()
    InitTrig_Race_BloodElves_O()
    InitTrig_Race_Dalaran_O()
    InitTrig_Race_KulTiras_O()
    InitTrig_Race_Nocnorogdennue_O()
    InitTrig_Race_Draeneis_O()
    InitTrig_Race_Vryculs_O()
    InitTrig_Race_KultSumMolota_O()
    InitTrig_Race_Nerubs_O()
    InitTrig_Race_Silitids_O()
    InitTrig_Race_Gnomes_O()
    InitTrig_Race_Gilneas_O()
    InitTrig_Race_Naga_O()
    InitTrig_Race_NightElf_O()
    InitTrig_Race_Forsaken_O()
    InitTrig_Race_Ogres_O()
    InitTrig_Race_Alliance_O()
    InitTrig_Race_JungleTrolls_O()
    InitTrig_Race_FelOrk_O()
    InitTrig_Race_ForestTrolls_O()
    InitTrig_Race_CultOfDamned_O()
    InitTrig_Race_Pandarens_O()
    InitTrig_Race_HordeW2_O()
    InitTrig_Race_Random_O()
end

-- ============================================================
-- Config (map settings)
-- ============================================================

function config()
    SetMapName("TRIGSTR_003")
    SetMapDescription("TRIGSTR_005")
    SetPlayers(24)
    SetTeams(24)
    SetGamePlacement(MAP_PLACEMENT_TEAMS_TOGETHER)

    -- Define 24 start locations
    DefineStartLocation(0, -9600.0, 19136.0)
    DefineStartLocation(1, 19520.0, -9024.0)
    DefineStartLocation(2, -9088.0, 21952.0)
    DefineStartLocation(3, 13568.0, -24064.0)
    DefineStartLocation(4, 3840.0, 24064.0)
    DefineStartLocation(5, -15808.0, 24640.0)
    DefineStartLocation(6, -20992.0, -1920.0)
    DefineStartLocation(7, 896.0, -12864.0)
    DefineStartLocation(8, -22400.0, 23616.0)
    DefineStartLocation(9, 18560.0, 24320.0)
    DefineStartLocation(10, -24640.0, 8320.0)
    DefineStartLocation(11, 15360.0, 5056.0)
    DefineStartLocation(12, 6208.0, -24128.0)
    DefineStartLocation(13, -4800.0, -29632.0)
    DefineStartLocation(14, -24128.0, -10944.0)
    DefineStartLocation(15, 17088.0, 4672.0)
    DefineStartLocation(16, 21824.0, -9088.0)
    DefineStartLocation(17, -20736.0, 20544.0)
    DefineStartLocation(18, -3776.0, -28544.0)
    DefineStartLocation(19, 17024.0, -24448.0)
    DefineStartLocation(20, 21056.0, 15872.0)
    DefineStartLocation(21, 12864.0, 16256.0)
    DefineStartLocation(22, -23424.0, -7040.0)
    DefineStartLocation(23, 5568.0, 4800.0)
end
