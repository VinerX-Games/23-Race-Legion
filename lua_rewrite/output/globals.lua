-- ============================================================
-- 23 Race Legion - Lua Rewrite
-- output/globals.lua — All global variables
-- ============================================================

_G.G = {} -- Global table for all migrated vJASS globals

-- ============================================================
-- Library globals
-- ============================================================

-- LIBRARY_AA
G.Counter = 0
G.EnemyCapital = nil

-- LIBRARY_Global
G.Global_Hash = {}       -- was hashtable, replaced with Lua table
G.Global_Timer = CreateTimer()
G.Global_TempGroup = CreateGroup()
G.Global_TempRect = Rect(0, 0, 0, 0)
G.Global_TempLoc = Location(0, 0)
G.Global___TempUnitArray = {}
G.Global___TempIntArray = {}
G.Global___TempRealArray = {}

-- LIBRARY_SpellSleepAOE
-- constants:
-- SpellSleepAOE___SpellHero = FourCC('A06P')
-- SpellSleepAOE___SpellCast = FourCC('A06O')
-- SpellSleepAOE___SpellOrder = "sleep"
-- SpellSleepAOE___DummyID = FourCC('u000')
-- SpellSleepAOE___DummyOwner = Player(PLAYER_NEUTRAL_PASSIVE)
G.SpellSleepAOE___DummyUnit = nil

-- LIBRARY_LibDifferentAiStuff
G.AiData = {}           -- was hashtable
G.AiUnitsToPort = {}
G.TryPort_pi = 0

-- LIBRARY_SanctifiedEnchantment
-- constants:
-- SanctifiedEnchantment_SkillId = FourCC('A1K0')
-- SanctifiedEnchantment_SkillBookId = FourCC('A1JU')
-- SanctifiedEnchantment_SkillAbilityStatusId = FourCC('A1JW')
-- SanctifiedEnchantment_SkillBuffStatusId = FourCC('B07Z')
-- SanctifiedEnchantment_AbilitySplashId = FourCC('A1JX')
-- SanctifiedEnchantment_MAXLVL = 4
G.SanctifiedEnchantment_BuffDuration = {}

-- LIBRARY_Races
G.tArray = {}
G.tB = 0
G.Grades = {}
G.AiCapitalGuard = {}
G.AiCapitalBuildigs = {}

-- ============================================================
-- udg_ globals (GUI-generated)
-- ============================================================

-- Economy
G.udg_Income = {}
G.udg_TEST = nil
G.udg_IncomeTimerFirst = nil
G.udg_IncomeTimerSecond = nil
G.udg_LocalOtrad = nil
G.udg_Korably = nil
G.udg_LocalReal = {}
G.udg_LocalspecialEffect = {}
G.udg_LocalPosition = {}
G.udg_LocalUnit = {}
G.udg_Flagmans = nil
G.udg_FlagmanEst = {}
G.udg_BuildEffectGroup = nil
G.udg_T2 = {}
G.udg_T3 = {}
G.udg_NaimEffectGroup = nil
G.udg_NalogUnit = nil
G.udg_Nalog = 0
G.udg_Stoimost = 0
G.udg_LocalInteger = 0
G.udg_Price = 0
G.udg_GoldCost = 0
G.udg_unit = nil
G.udg_GlobalGroups = {}
G.udg_TimerSecond = nil
G.udg_LocalText = nil
G.udg_LocalPlayer = nil
G.udg_ZahvatBuildings = nil
G.udg_effect = nil
G.udg_Spell = nil
G.udg_SilitidsLichinki = nil
G.udg_Table = nil
G.udg_PlayerScoreArmy = {}
G.udg_BuildedSctructure = {}
G.udg_TimerToDis = nil
G.udg_wawt = 0
G.udg_Kokon = nil
G.udg_SpawnLichinok = {}
G.udg_Kol_voUnitod = 0
G.udg_StolicaGroups = nil
G.udg_Vassals = {}
G.udg_TunnelGroup = {}
G.udg_playersingame = 0
G.udg_numberofforces = {}
G.udg_forces = {}
G.udg_Timer = nil
G.udg_peasants = {}
G.udg_dammis = nil
G.udg_Untitled_Variable_001 = {}
G.udg_AllPlayers = nil
G.udg_Skin = ""
G.udg_Dm = {}
G.udg_UU1 = {}
G.udg_Drain_Interval = {}
G.udg_z = 0
G.udg_Drain_Life_Max = 0
G.udg_zLoc = nil
G.udg_i2 = 0
G.udg_loc = nil
G.udg_Drain_Value = {}
G.udg_Drain_Range = {}
G.udg_y2 = 0
G.udg_x2 = 0
G.udg_y = 0
G.udg_x = 0
G.udg_i = 0
G.udg_Drain_Life_Lightning = {}
G.udg_Drain_Targets = {}
G.udg_Drain_Caster = {}
G.udg_Drain_Max = 0
G.udg_SSspecialeffect = {}
G.udg_SSfacing = {}
G.udg_SS = {}
G.udg_SSdamage = {}
G.udg_SSpointpicked = {}
G.udg_SSeffect = {}
G.udg_SSpointmovepicked = {}
G.udg_SSpointmovecaster = {}
G.udg_SStargetpoint = {}
G.udg_SSpointcaster = {}
G.udg_SSgroup = {}
G.udg_SSpicked = {}
G.udg_SScaster = {}
G.udg_SSinteger = {}
G.udg_HandleBoard = nil
G.udg_TempGroup = nil
G.udg_Boolexpr = nil
G.udg_LocalOtrad2 = nil
G.udg_AllPlayers2 = nil
G.udg_LocalForce = nil
G.udg_LocalText2 = ""
G.udg_SilitidTimer = nil
G.udg_LocalReal2 = 0
G.udg_LocalPosition2 = nil
G.udg_ChargeTimer = nil
G.udg_LocalUnit2 = nil
G.udg_LCode = nil
G.udg_Inc = 0
G.udg_l = 0
G.udg_PlayerTableNumber = {}
G.udg_LocalOtrad3 = nil
G.udg_LocalPosition3 = nil
G.udg_Visibl = {}
G.udg_PlayersCount = 0
G.udg_UnitsCount = {}

-- Portal
G.udg_Portal_INDEX_CASTER = 0
G.udg_Portal_INDEX_TARGET = 0
G.udg_Portal_INDEX_TRAVELLER = 0
G.udg_Portal_ConfigIndex = {}
G.udg_Portal_dummy = nil
G.udg_Portal_range = {}
G.udg_Portal_delay = {}
G.udg_Portal_delayFXAbil = {}
G.udg_Portal_missileSpeed = {}
G.udg_Portal_missileHeight = {}
G.udg_Portal_active = {}
G.udg_Portal_FX = {}
G.udg_Portal_activeFX = {}
G.udg_Portal_departureFX = {}
G.udg_Portal_arrivalFX = {}
G.udg_Portal_loc1 = nil
G.udg_Portal_loc2 = nil
G.udg_Portal_loc3 = nil
G.udg_Portal_loc4 = nil
G.udg_Portal_portal = {}
G.udg_Portal_targeted = {}
G.udg_Portal_traveller = nil
G.udg_Portal_group = nil
G.udg_Portal_teleMissiles = nil
G.udg_Portal_missileDummy = {}
G.udg_Portal_preventAllies = {}
G.udg_Portal_missileFXAbil = {}
G.udg_Portal_SeverAbility = 0
G.udg_Portal_isTeleporting = {}
G.udg_Portal_missileTargetable = {}
G.udg_Portal_missileUseOwnMovement = {}

-- Unit Indexer
G.udg_UDex = 0
G.udg_UDexRecycle = 0
G.udg_UDexNext = {}
G.udg_UDexGen = 0
G.udg_UDexUnits = {}
G.udg_UDexPrev = {}
G.udg_UnitIndexEvent = 0
G.udg_UnitIndexerEnabled = false
G.udg_UDexWasted = 0

-- Misc
G.udg_Unit = {}
G.udg_LocalEffect = nil
G.udg_Continents = {}
G.udg_LocalUnit3 = nil
G.udg_LobbyTime = nil
G.udg_LobbyTimerWindows = nil
G.udg_GameMode = 0
G.udg_Total_hero = 0
G.udg_Random_system = {}
G.udg_Random_Hero = 0
G.udg_Players_hero = nil
G.udg_SET_TimerTime = 0
G.udg_SET_VISIBLE_MODE = 0
G.udg_F_Group = {}
G.udg_LocalInteger2 = 0
G.udg_LocalInteger3 = 0
G.udg_Tier = {}
G.udg_LocalPlayer2 = nil
G.udg_ElemCount = {}
G.udg_TierLevel = {}
G.udg_NewChargeTimer = nil
G.udg_TechResearched = {}
G.udg_MAX_TECH_RESEARCHES = 0
G.udg_TechId = 0
G.udg_UnitGelbin = {}
G.udg_LocCircle = nil
G.udg_AiControl = {}
G.udg_Bots = nil
G.udg_LocalPoint = nil
G.udg_Ai_units = {}
G.udg_Ai_builders = {}
G.udg_Ai_buildings = {}
G.udg_TimerSmall = nil
G.udg_TimerSmall2 = nil
G.udg_TimerSmall3 = nil
G.udg_AiTimerStrateg = nil
G.udg_Octhet = false
G.udg_CityNearWater = nil
G.udg_LocalInteger4 = 0
G.udg_LocalInteger5 = 0
G.udg_Ai_buildersT = {}
G.udg_Ai_army = {}
G.udg_Ai_harvest = {}
G.udg_Ai_navy = {}
G.udg_TimerToChangeAi = nil
G.udg_HeroFirstYes = {}
G.udg_HordeLandPrice = {}
G.udg_MainPrice = {}
G.udg_HordeElitePrice = {}
G.udg_HordeNavyPrice = {}
G.udg_HordeMagicPrice = {}
G.udg_HordeTechPrice = {}
G.udg_TombOfSargeras = nil
G.udg_FacelessLumberBuildings = nil

-- Transport
G.udg_LoadedGroup = nil
G.udg_TransportingGroup = nil
G.udg_StopOrder = 0
G.udg_TransportingIncrement = 0
G.udg_TransportingMin = 0
G.udg_TransportingUnitArray = {}
G.udg_LoadedGroupArray = {}
G.udg_TempUnit02 = nil
G.udg_TempUnit01 = nil
G.udg_TestUnit = nil
G.udg_Caster = nil
G.udg_Dummy = {}
G.udg_Target = nil
G.udg_To4kaCaster = nil
G.udg_To4kaDummy = nil
G.udg_Logika = false
G.udg_HisloA = {}
G.udg_Ygol = {}
G.udg_Timer_Copy = nil
G.udg_LogikaCast = false
G.udg_To4kaTarget = nil
G.udg_Group = nil
G.udg_To4kaAOE = nil
G.udg_u = nil
G.udg_u_Copy = nil
G.udg_To4kaTarget_Copy = nil

-- Eye spells (Russian: Глаз)
G.udg_Dalnost_R_Glaz = {}
G.udg_Group_R_Glaz = {}
G.udg_Dummy_R_Glaz = {}
G.udg_Caster_R_Glaz = {}
G.udg_Timer_R_Glaz = nil
G.udg_To4kaDummy_R_Glaz = {}
G.udg_To4kaCaster_R_Glaz = {}
G.udg_S4et_R_Glaz = {}
G.udg_Cikl_R_Glaz = 0
G.udg_Antibag_R_Glaz = {}
G.udg_MUI_R_Glaz = 0
G.udg_Logika_R_Glaz = {}
G.udg_Dalnost_E_Glaz = {}
G.udg_Timer_E_Glaz = nil
G.udg_Group_E_Glaz = {}
G.udg_To4kaCaster_E_Glaz = {}
G.udg_Caster_E_Glaz = {}
G.udg_Cikl_E_Glaz = 0
G.udg_Antibag_E_Glaz = {}
G.udg_MUI_E_Glaz = 0
G.udg_Logika_E_Glaz = {}
G.udg_S4et_W2_Glaz = {}
G.udg_Logika_W2_Glaz = {}
G.udg_To4kaTarget_W_Glaz = {}
G.udg_To4kaCaster_W_Glaz = {}
G.udg_Group_W_Glaz = {}
G.udg_Caster_W_Glaz = {}
G.udg_Timer_W_Glaz = nil
G.udg_S4et_W_Glaz = {}
G.udg_Cikl_W_Glaz = 0
G.udg_Antibag_W_Glaz = {}
G.udg_MUI_W_Glaz = 0
G.udg_Logika_W_Glaz = {}
G.udg_DummySe_Q_Glaz = {}
G.udg_Wait_Q_Glaz = {}
G.udg_Range_Q_Glaz = {}
G.udg_S4et_Timer_Q_Glaz = {}
G.udg_To4kaTarget_Q_Glaz = {}
G.udg_To4kaCaster_Q_Glaz = {}
G.udg_Group_Q_Glaz = {}
G.udg_Dummy_Q_Glaz = {}
G.udg_Caster_Q_Glaz = {}
G.udg_Timer_Q_Glaz = nil
G.udg_Antibag_Q_Glaz = {}
G.udg_Cikl_Q_Glaz = 0
G.udg_Logika_Q_Glaz = {}

-- Continue globals (350+)
G.udg_HisloA_S = {}
G.udg_Zirbyl_Govnolol = 0
G.udg_A_pol_Reg_on_disable = nil
G.udg_pol_Reduce = nil
G.udg_A_pol_Volna = nil
G.udg_A_pol_Volna_Unit = nil
G.udg_Arthas_Predaki_Model_Standart = ""
G.udg_Arthas_Predaki_Model = ""
G.udg_Arthas_Palabot = 0
G.udg_Arthas_Unit_First = nil
G.udg_Arthas_Unit_Second = nil
G.udg_Arthas_Unit_Paladin = nil
G.udg_Arthas_To4ka = nil
G.udg_Sheid = {}
G.udg_Arthas_Soul = {}
G.udg_Arthas_Soul_To4ka = {}
G.udg_BotsActive = nil
G.udg_BotsActiveB = nil
G.udg_TimerSmall4 = nil
G.udg_PlayerGet1 = nil
G.udg_PlayerGet2 = nil
G.udg_PlayerGet4 = nil
G.udg_AiFixer = nil

-- Game state variables (arrays)
G.income = {}
G.incomeW = {}
G.disincome = {}
G.logistic = {}
G.corruption = {}
G.balance = {}
G.additional = {}
G.IncomeMod = 1.0
G.Tax = 0.15
G.AllyTax = {}
G.DisOn = false
G.EcLog = false

-- Capital system
G.playerCapital = {}
G.Capital = {}
G.cap_time = {}
G.Vassals = {}
G.Senior = {}
G.CityCount = 0
G.CityPlayerCount = {}
G.PercentWin = 65

-- Diplomacy
G.DipMode = 2

-- AI difficulty
G.AiMoney = 7
G.AiMass = 5
G.AiRepeat = 5
G.AiRadius = 6
G.AiLimit = 150

-- Scratch globals (g-prefixed, used in filter functions for perf)
G.gUnit = nil
G.gInt = 0
G.gX = 0
G.gY = 0
G.gPlayer = nil
G.gPi = 0

-- Magic constants
G.JASS_MAX_ARRAY_SIZE = 32768
