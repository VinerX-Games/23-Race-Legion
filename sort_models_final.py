"""Sort root models into race subdirectories, rebuild war3map.imp via HiveWE."""
import os
import shutil
import subprocess
import json
import re

MAP_DIR = os.path.join(os.path.dirname(__file__), "map.w3x")
HIVE_CLI = r"C:\Games\HiveWE_VinerX_Edition\build\Release\Release\HiveWE_cli.exe"

RACE_PATTERNS = {
    "Alliance": ["Admiral", "Ballista", "Captain", "Cannon Ball", "Chaplain", "Human",
        "Mage_1", "Mage_Portrait", "Militia", "Musketman", "Paladin-from-WoW",
        "PeasantFemale", "PriestessOfTheTides", "Revive Altar",
        "Royal", "squire", "statue", "Arthas", "Brigitte_Abbendis",
        "Forge", "Farm3", "GoodCastle", "HJar", "Highaltar", "ShieldHands",
        "Danath Trollbane", "Hero_Paladin", "HolyRuneGuardian",
        "LightforgedHammerHero", "Mounted Captain", "RuneGuardian", "Dsorceress",
        "Lightforged", "Bishop", "Crusader", "Garrison", "Marwyn",
        "Footman", "Judgment", "Knight", "Lord Admiral", "Peasant",
        "Priest.mdx", "Priest_Portrait", "Tidesage", "Priest",
    ],
    "Scarlet": ["Scarlet", "Renault", "Sally", "Saidan", "saidandathrohan",
        "Calia_Menethil", "Herod"],
    "Horde": ["Horde", "Orc", "Durotan", "Grommash", "Guldan", "Chogall",
        "Teron", "ChaosOrc", "DeathKnightWC2", "BlackhandsFang", "HeroMageWC2",
        "ArmoredDireWolf", "DireWolf", "Dragons Reach", "D3 Barbarian",
        "Quilboar", "Shama", "Thunderlord", "LaughingSkull", "Garrosh",
        "Blackrock", "FrostwolfOrc", "Dragonmaw", "IronStar",
        "Grunt", "DemolisherIronHorde", "Rend", "Varok", "Frostwolf",
        "HeroMageWC2", "FrostwolfOrc",
    ],
    "FelOrk": ["FelOrc"],
    "Trolls": ["TrollJ", "TrollV", "TrollH", "DireTroll", "ForestTroll",
        "ftroll_", "HeroTroll", "HeroVoodoo",
        "Atalai", "Bwonsamdi", "Hakkar", "Voljin", "Zuljin",
        "AltarOfLoa", "AltarofBlood", "BarracksGurubashi", "Beastiary",
        "BurrowGurubashi", "GreatHallGurubashi", "SpiritLodgeGurubashi",
        "WarMillGurubashi", "Skullsplinter", "ZuldrakGolem",
        "TrollHexer", "TrollWarrior", "TrollMageJg", "TrollShaman",
        "TrollWorker", "TrollGatherer", "Troll_Hall", "TrollCatapult",
        "TrollConjurer", "TrollBonecaster", "Troll MageMask",
        "TwilightRage", "RighteousFury", "BloodCultistMissile",
        "BlueBlood", "FelBlood", "EliteHeadhunter",
        "CursedSTR", "DarkRedGlow", "OrcLumberMill",
        "Redsplash", "UDeathBlood",
    ],
    "Forsaken": ["Banshee", "Sylvanas", "Nathanos", "TheBanshee",
        "Lich", "TheLich", "The Deathbringer", "Koltira",
        "DarknessRising", "HeroCryptWarlock", "CryptMother",
        "Firefly_CryptLord", "Undean", "UndeadAltar", "UndeadBark",
        "UndeadShip", "CitizenLordaeronUndead", "Jailer",
        "ValkyrDark", "Northrend", "WretchedWorker",
        "Forsaken", "Undead", "GrandApothecary", "SC_Rogue",
        "Spore", "DarknessEssence", "WotLK", "TempleOfTheDamned",
    ],
    "BloodElf": ["BloodElf", "Bloodelf", "Blood_Elf", "BE_",
        "Hawkstrider", "KaelStatue", "Lorthemar", "Lady Liadrin",
        "Sunwell", "HighElf", "BEDragon", "ElvenBarracks", "ElvenFarm",
        "ElvenForge", "ElvenMagicTower", "KArchSorceress",
        "RuinedElf", "ElfWarrior", "vareesa", "QuelThalas",
        "ArcaneGuardFel", "BloodelfChampion", "Bloodelf_Cavalry",
    ],
    "Nightelfs": ["NightElf", "NE ", "Nelf", "NE_", "NEDungeon",
        "Cenarius", "CorruptedDryad", "Corrupted_Ancient",
        "MoonBowl", "MoonPriestess", "Wisp", "Ashenvale",
        "ElfMill", "ElfStage", "Nightsaber", "GlaiveMaiden",
        "DismountedHuntress", "Preserver", "FlowerDryad",
        "NelfDruidCat", "Fountainhead", "AncientofLies",
        "HeroElvenDemonHunter", "Dark Elven Archon", "Wardancer",
        "LegendaryPriestess", "VillagerDruid", "203_NightElf",
    ],
    "Naga": ["Naga", "TempleofTides", "NagaMedusa", "NagaPortal",
        "NagaRoyal", "NagaTrident",
    ],
    "DemonsOrLegion": ["Demon", "Demonic", "Archimonde", "Kiljaeden",
        "Sargeras", "LordArchimonde", "Infernal", "Inferal",
        "FelGuard", "FelShivarra", "FerSZ", "ShadowShivarra",
        "EvilMedivh", "MoargBrute", "VoidWalker", "Void Rift",
        "DemonicGateway", "Portal", "GreenShimmeringPortal",
        "AstroSatyr", "Satyr", "HeroSatyr", "KeeperFerSZ",
        "KeeperNightmareFerSZ", "InquisitorN", "Archfiend",
        "Hero_Felreaper", "Hero_Inquisitor", "GenesaurGreen",
        "GrimWard", "Felbolt", "FelS",
    ],
    "Dragon": ["Dragon", "Deathwing", "Drake", "BlueDragonNexus", "Simurgh"],
    "Silitids": ["Silitid", "Silithid", "silithid", "Anubisath",
        "Forgotten", "Quiraj", "RockBorer", "TwinEmperor", "BattleGuard",
        "HiveTentacles", "SilithidScarab", "SilithidTank", "Silithid_",
        "SilithidHive", "web1", "web2",
    ],
    "E_Elementals": ["Earth", "Crystal", "Firemage",
        "Fire Totem", "Firework", "Flamethrower",
        "FrostSpawn", "Frosty Crystal Drop", "Lava", "PillarOfIce",
        "Water Totem", "WaterPlane", "WindTotem", "MAGII KOLODEC",
        "FirePandaren", "EarthPandaren", "StormPandaren", "WoodPandaren",
    ],
    "IceTrolls": ["IceTroll", "IceBerserker", "IceBone", "HeroIce",
        "IceUndeground", "IceAltar", "IceBlacksmith", "IceSpirit",
        "FrostWind", "FrostWinter", "Burrow_", "Trundle",
        "HeroTrollGodslayer",
    ],
    "Goblins": ["Goblin", "GoblinTPM", "GoblinSteamboat",
        "FlamerGoblin", "AmmoDump", "BeastPit", "BombCart",
        "Brawler", "CruiseMissile", "Daimler", "EnbarcacionGoblin",
        "FlameShredder", "GobAltar", "GoblinBarracks", "GoblinEngineer",
        "GoblinFuelPump", "GoblinHammerhead", "GoblinHovercraft",
        "GoblinMedic", "GoblinOutpost", "GoblinRocketeer", "GoblinScout",
        "GoblinSoldier", "GoblinSub", "GoblinTinkerTurret",
        "GoblinTommygunner", "GoblinTower", "Goblin_Assault",
        "Goblin_Flame", "GobTrainingCenter", "HeavyShredder",
        "HeroGoblinGunner", "junkyard", "NewGroundEX",
        "Rocket", "SpaceOrc", "templeofboom",
        "Artillery", "Artillery Shell",
    ],
    "Gnomes": ["Gnome", "Gnomer", "Clockwerk", "MadScientist", "Generator",
        "BU_Generator", "KB_Cannon", "ATank", "Automaton", "Bombardier",
        "Canon_Turret", "ClapTrap", "DwarfArtillery", "DwarfFlameTank",
        "DwarfScoutTank", "DwarfTechWorker", "DwarvenAnti-Air",
        "Effect_MechanicGears", "Engineer", "GearAura",
        "GnomishRifleman", "GnomishSpiderTank", "Konous",
        "Mr. Steampunk", "Robot", "Shield Hand",
        "Steamfortress", "Steampunk", "SteamSpider", "Thunder_Tower",
        "Warlock", "Nuclear",
    ],
    "Gnomers": ["Gelbin", "NuclearExplosion", "Hero_Gelbin"],
    "Dwarfes": ["Dwarf", "MorganIronhand", "Magni", "HeroArchMaiden"],
    "Ogre": ["Ogre", "Drillmo", "Gronn", "Gruul", "HeroOgre",
        "LordOrbough", "OgreDoom", "OgreDrummer", "OgreHunter",
        "OgreJad", "OgreLud", "OgreMage", "OgreMauler",
        "OgreThrower", "ogrewarlock", "OgreWarlord", "Ogron",
        "Undeground", "Watchtower", "WCI", "Zakroma",
        "Shaman.mdx",
    ],
    "Pandarens": ["Pandaren", "Pandaria", "Dojo_", "Ninjapan",
        "ShodoPan", "Yangu", "Sumo", "Tiki", "DruidOfThePanda",
        "AltarOfMasters", "BreathOfFire", "BrewCloud",
        "BuildingPandarenTower", "Disarm", "dummy",
        "Fear", "Fissure", "Geomancer_E", "HeroShadoPan",
        "Hero_IronFist", "KyoWarrior_E", "Model_Builder_Panda",
        "Pandamonium", "Pandan_", "PandaQ", "PandarenBattleship",
        "PandarenBig", "PandarenMilitia", "PandarenMonk",
        "PandarenNoble", "PandarenRunemaster", "PandarenSage",
        "PandarenTemple", "PandarenTiger", "PandarenTransport",
        "PandarenTree", "Pandaren_", "Pandarian",
        "PandaRider", "RockSlam", "RollingKeg",
        "Taunt", "WarDancer", "WindBlow", "ZapMissile",
    ],
    "Kul-Tiras": ["KulTiras", "Kultiras", "JainaProudmoore", "Jaina",
        "TudorCaravel", "PirateBrig", "BattleshipKul", "Cannoneer",
        "Flibustier", "Footman_Kul", "Guardsman_Kul", "Knight_Kul",
        "KultirasAltar", "KultirasArcane", "KultirasBarracks",
        "KultirasBlack", "KultirasChapel", "KultirasCity",
        "KulTirasDread", "KultirasHouse", "KultirasLumber",
        "KultirasShip", "KultirasTower", "KultirasTown",
        "KultirasWork", "Rifleman_Kul", "Royal Guard_Kul",
        "Ships_Doctor", "Storm_Sorcerer",
    ],
    "Worgens": ["Worgen", "Gilneas", "AxemanGilneas",
        "BattleshipGilneas", "Werewolf", "Lycan", "Beowulf",
        "Genn Greymane", "GilneasAltar", "GilneasBarracks",
        "GilneasBlack", "GilneasFarm", "GilneasLumber", "GilneasManor",
        "GilneasTower", "GilneasTown", "GilneasTrade", "WereWolf",
    ],
    "Faceless": ["Faceless", "FacelessOne", "Temple of Faceless",
        "Nzoth", "YoggSaron", "Cthun", "ForgottenOne",
        "GeneralVezax", "Mindflayer", "TentaclePit",
    ],
    "Sromgard": ["Strom", "Arathi", "Danath", "BanditSpear",
        "HeroArchMage(Nicam)", "HeroPaladin(Nicam)",
        "Knight(Nicam)", "Priest(Nicam)", "Stromgarde",
    ],
    "CultOfDamned": ["Cult", "Damned", "Blight", "Plague", "BloodSlam",
        "Black Garden", "BlackKeep2", "8bl_cultist", "twilightshammer",
        "Black Decay", "Black Missile", "Black Mist",
    ],
    "SkeletsDifferent": ["Skelet", "Bone", "Drill Sergeant", "Skull", "Banisher"],
    "Bandits and Westfall": ["Bandit", "Westfall", "Crossbowman",
        "HeroRogue", "Rogue", "Assasin", "Deadeye", "ShadowWarrior",
    ],
    "Dalaran": ["Dalaran", "Rhonin", "Violet", "Khadgar", "Hero_Khadgar",
        "ArcaneCastle", "ArcaneCathedral", "ArcaneWell",
        "Aegisary", "Aether Vault", "Mystic Loom", "Scrying_Tower",
        "Tesseract", "Kupol", "Sorceress3", "MChanneler",
        "Lyceum Arcana", "HeroChronomancer", "Tempomancer",
        "Emporium 13", "Archmage", "dalaran",
    ],
    "DraeneiMisc": ["Draenei", "Dranai", "Velen", "Prophet Velen",
        "Vindicator", "Maraad", "LightReaver", "Naaru", "Elekk",
        "Akama", "VicaressofElune", "Adherent", "Gemcrafter",
        "Luminary", "VaultOfRelics",
    ],
    "VrykulMisc": ["Vrykul", "HeroVrykul"],
    "NerubianMisc": ["Nerubian", "Firefly_Nerubian", "HeroNerubian",
        "HeroSpiderLord", "SandReaver_CryptLord",
        "Wasp_CryptLord", "Wasp_SpiderLord",
    ],
    "Illidari": ["Illidari"],
    "LostOnes": ["LostOne"],
    "Embers": ["Ember"],
    "Auras": ["Aura "],
    "Missiles": ["Missile", "Bullet_", "Chain Grenade", "Chaos Missile",
        "Demonic Missile", "Faerie Missile", "Felbolt",
        "Fire Crescent", "Fire Spear", "FireArrow", "Fireball",
        "Firebolt", "Grenade", "Hammer Missile", "Holy Missile",
        "LightningMissile", "PotatoMasher", "PrismBeam",
        "SHIVA", "Shock Blast", "Shot ", "Sonic Missile",
        "Spectral Missile", "Sword Missile", "Tank Shell",
        "Void Arrow", "Void Crescent", "Void Spear", "Voidball",
        "Voidbolt", "Wizardry Missile",
        "Axe Missile", "Mace Missile",
    ],
    "NewEffects": ["Culling", "Valiant", "Blood_Presence",
        "Unholy Presence", "Glow", "StarBreathDamage", "DetroitSmash",
        "Blood Ritual", "Aurum Beam", "Shining Flare", "Rain of Fire",
        "IonCannon", "ForceField", "BirthMesh", "Nether Blast",
        "priestespellnode", "Soul Discharge",
        "Malevolence Aura", "Frost Presence", "Darkness",
        "DarkFrenzy", "HealTarget", "VampiricAura",
        "StampedeMissile", "Stampede", "SparkleStampede",
        "Star5tgaStampede", "StarStampede", "SunStampede",
        "TeamGlowStampede", "WaterStampede",
        "WhiteBoneDust", "WhiteGlow", "SapStampede",
        "ShadowStampede", "LavaStampede", "LightFlare",
        "LightningStampede", "FlareStampede", "DustStampede",
        "BlackBone", "BlueGlow", "DarkerBlack",
    ],
    "Common": ["Floating_Islands", "LoadingScreen", "GeneralHeroGlow",
        "PurpleCrystal", "Pyramide", "Shrine3", "Stormbell",
        "Witness", "Shaper", "WarpRingless", "BearTrap",
        "LatestRowboat", "Owl", "TombOfRelics", "Trebupult",
        "Venolia", "Champion of the Uncrowned", "DayLaborer",
        "Laborer", "Ranger", "sentrygun", "dhouse", "EastBuilding",
        "EgyptionTomb", "EegNest", "FrozenDomain",
        "Mordor Gate", "PowerGenerator", "Soul Armor", "Soul_Armor",
        "UmbarBlackShip", "FlyBarracks", "HeroVialHeart",
        "Theo", "none2", "Magic Ball", "Magic Barracks", "MagicVault",
        "Altar of Starlight", "AltarOfDalar", "AltarOfHonor",
        "AltarOfTheSpider", "Ancient Guard7", "AncientAltar",
        "AncientBeast", "AncientTemple", "AncientTower", "AncientVault",
        "AncientWarrior", "TempleOfTheDamned5",
    ],
    "Doodads": ["Bush", "cloud_big", "cloud_tcfix",
        "FinePine", "NewOak", "HaloDeadTree", "PlagueLandTree",
        "AshenvaleTree", "QuelThalas", "NorthrendFissure",
        "MetalChunk", "CoralBed", "OceanReef", "OrcOilTanker",
        "bce837996801f3a3", "final_export2", "FreyaNEW",
    ],
    "Walls": ["City_Wall", "Gondolian_Wall",
        "wallpiece", "wallpost", "gate0", "Cityscape Stairs",
        "StoneBridge", "Doodad_Pillar", "Doodad_SmallWall",
        "Doodad_Wall",
    ],
    # Catch-all patterns for files that have race-specific prefixes in root
    "EntCorrupted": ["Corrupted_AncientOfLies", "CorruptedDryad",
        "HeroCorruptedEant", "HeroEant", "HeroForestLord",
        "ForestBlessing", "NatureBlessing", "Natures Ward",
        "NaturesWrath", "AncientBeast(life)",
        "AncientofLoreCorrupted", "AncientofWindCorrupted",
        "CorraptedAncientBeast", "FaerieDragonAncient",
        "WispEvil", "HighMage", "Kiper",
        "CorruptedAncientBeast", "BloodMage.mdx",
        "HeroHighElfAssassin", "GenesaurGreen",
    ],
    "IceTrolls2": ["IceTroll", "FrostWind", "FrostWinter",
        "IceUndeground", "IceBone", "IceAltar", "IceBlacksmith",
        "IceSpirit", "Burrow_", "HeroIce", "Trundle",
        "TrollCatapult.mdx", "TrollCatapultMissile",
        "TrollConjurer.mdx", "TrollBonecaster", "NagaSerpent",
        "HeroTrollGodslayer",
    ],
}


def get_race(filename):
    base = os.path.splitext(filename)[0]
    base_lower = base.lower()
    for race, patterns in RACE_PATTERNS.items():
        for pat in patterns:
            if base_lower.startswith(pat.lower()):
                if race.endswith("2"):  # merged pattern sets
                    return race[:-1]
                return race
    return None


def move_files():
    root_models = []
    for f in os.listdir(MAP_DIR):
        fp = os.path.join(MAP_DIR, f)
        if os.path.isfile(fp) and f.lower().endswith(('.mdx', '.mdl')):
            root_models.append(f)

    matched = 0
    unmatched = []
    moves = {}

    for m in sorted(root_models):
        race = get_race(m)
        if race:
            dest_dir = os.path.join(MAP_DIR, race)
            os.makedirs(dest_dir, exist_ok=True)
            src = os.path.join(MAP_DIR, m)
            dst = os.path.join(dest_dir, m)
            shutil.move(src, dst)
            moves[m] = race
            matched += 1
        else:
            unmatched.append(m)

    print(f"Root models: {len(root_models)}")
    print(f"Moved: {matched}")
    print(f"Left in root: {len(unmatched)}")
    if unmatched:
        print("Unmatched:")
        for u in unmatched:
            print(f"  {u}")

    return matched, unmatched, moves


def update_war3map_lua(moves):
    """Update model path references in war3map.lua."""
    lua_path = os.path.join(MAP_DIR, "war3map.lua")
    if not os.path.exists(lua_path):
        print("war3map.lua not found, skipping")
        return

    with open(lua_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    count = 0
    for filename, race in moves.items():
        old_str = filename
        new_str = f"{race}/{filename}"
        if old_str in content:
            content = content.replace(old_str, new_str)
            count += content.count(new_str) - content.count(old_str) + 1

    with open(lua_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated war3map.lua: ~{count} reference(s) changed")


def rebuild_imp():
    """Regenerate war3map.imp from directory listing."""
    # war3map.imp is a simple text file listing all imported files
    imp_path = os.path.join(MAP_DIR, "war3map.imp")
    lines = []
    for root, dirs, files in os.walk(MAP_DIR):
        for f in files:
            full = os.path.join(root, f)
            rel = os.path.relpath(full, MAP_DIR).replace('\\', '/')
            # Skip map internal files
            if any(rel.startswith(s) for s in ('_lua/', '_Locales/', '_cli_',
                    'war3map.', 'war3mapSkin.', 'war3mapMap.blp',
                    'war3mapExtra.txt', 'war3mapMisc.txt')):
                continue
            # Skip known non-import directories
            if any(rel.startswith(s) for s in ('UI/', 'ReplaceableTextures/',
                    'Textures/', 'TerrainArt/', 'ent/')):
                continue
            lines.append(rel)

    with open(imp_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(lines)) + '\n')

    print(f"Rebuilt war3map.imp: {len(lines)} entries")


if __name__ == '__main__':
    print("Step 1: Moving model files...")
    matched, unmatched, moves = move_files()

    print("\nStep 2: Updating war3map.lua references...")
    update_war3map_lua(moves)

    print("\nStep 3: Rebuilding war3map.imp...")
    rebuild_imp()

    print("\nDone!")
