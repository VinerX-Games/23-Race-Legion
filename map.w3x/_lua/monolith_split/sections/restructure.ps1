$ErrorActionPreference = "Stop"
$root = "C:\Games\23 Race\23-Race-Legion\map.w3x\_lua\monolith_split\sections"
$sourceFile = Join-Path $root "80_generated_runtime.lua"
$outDir = Join-Path $root "80_runtime"
$manifestPath = Join-Path $root "..\manifest.json"

# ── read source ──
Write-Host "Reading source..."
$encoding = [System.Text.UTF8Encoding]::new($false)
$sourceBytes = [System.IO.File]::ReadAllBytes($sourceFile)
$sourceText = $encoding.GetString($sourceBytes)
$lines = $sourceText -split '\r?\n'
while ($lines.Count -gt 0 -and $lines[-1] -eq '') { $lines = $lines[0..($lines.Count-2)] }
Write-Host "$($lines.Count) lines, $($sourceBytes.Count) bytes"

# ── create output structure ──
if (Test-Path $outDir) { Remove-Item -LiteralPath $outDir -Recurse -Force }
$subdirs = @("_infra", "_lib", "_player", "_ui", "_races", "_ai", "_continental", "_features", "_data", "triggers")
foreach ($d in $subdirs) { New-Item -ItemType Directory -Path (Join-Path $outDir $d) -Force | Out-Null }

function Write-LuaFile($relPath, $lineArr) {
    $raw = ([string]::Join("`r`n", $lineArr) + "`r`n")
    [System.IO.File]::WriteAllBytes((Join-Path $outDir $relPath), $encoding.GetBytes($raw))
}

# ── find all section boundaries (same as original split_80 script) ──
$sectionMap = [ordered]@{
    "Global Variables" = "_infra/10_globals.lua"
    "Custom Script Code" = "_infra/20_custom_script.lua"
    "Counter" = "_infra/30_player_counter.lua"
    "gGlobal objects" = "_infra/40_bool_exprs.lua"
    "LibNewFunctions" = "_lib/50_lib_new_functions.lua"
    "UpdateGraph" = "_lib/51_update_graph.lua"
    "Enter" = "_lib/52_enter.lua"
    "Settings" = "_lib/53_income_settings.lua"
    "CountAddDis and CountDelDis" = "_lib/54_count_dis.lua"
    "ClearEc" = "_lib/55_clear_ec.lua"
    "ClearPlayer" = "_lib/56_clear_player.lua"
    "TimedUpdate" = "_lib/57_timed_update.lua"
    "InitThings" = "_lib/58_init_things.lua"
    "PlayerUI" = "_ui/59_ui_setup.lua"
    "IncomeTooltip" = "_ui/60_income_tooltip.lua"
    "AllPlayersStart" = "_player/61_all_players.lua"
    "CommonHash" = "_lib/62_common_hash.lua"
    "ClearAllies" = "_player/63_clear_allies.lua"
    "DelUnitStart" = "_player/64_del_unit.lua"
    "RandomLocationFromUnits" = "_player/65_random_locs.lua"
    "CreateRaceCircles" = "_player/66_race_circles.lua"
    "CityCountCheck" = "_player/67_city_check.lua"
    "SubGroup2" = "_player/68_subgroup2.lua"
    "Pstart" = "_races/70_race_farm_start.lua"
    "CountForTier" = "_races/71_tier_system.lua"
    "ChangeSpellLimit" = "_races/72_farm_limit.lua"
    "HordeW2On" = "_races/73_horde_w2.lua"
    "XpLevelW2" = "_races/74_w2_xp.lua"
    "CultOn" = "_races/75_cult_on.lua"
    "StartForestTrolls" = "_races/76_forest_trolls.lua"
    "StartJungleTrolls" = "_races/77_jungle_trolls.lua"
    "ForsacenOn" = "_races/78_forsaken_on.lua"
    "BuildingTierSystem" = "_races/79_building_tier.lua"
    "DragonsOn2" = "_races/80_dragons_on.lua"
    "ElemOn" = "_races/81_elem_on.lua"
    "PointAi" = "_ai/82_ai_points.lua"
    "TurnOffAi" = "_ai/83_turn_off_ai.lua"
    "Globals And Start setttings" = "_ai/84_globals_start.lua"
    "LibDifferentAiStuff" = "_ai/85_lib_ai_stuff.lua"
    "LibRaces" = "_ai/86_lib_races.lua"
    "ContinentalBoolexrs" = "_continental/90_continental_bool.lua"
    "ContinentalTemplates" = "_continental/91_continental_templates.lua"
    "Dungeons" = "_continental/92_dungeons.lua"
    "ContinentalMain" = "_continental/93_continental_main.lua"
    "TryToAttack2 Uni" = "_ai/94_ai_attack.lua"
    "TryToAttackN Uni" = "_ai/95_ai_attack_naval.lua"
    "KilledCity" = "_ai/96_ai_killed_city.lua"
    "GoToWater" = "_ai/97_ai_water.lua"
    "TryToBuild" = "_ai/98_ai_build.lua"
    "AiUnitJoins" = "_ai/99_ai_unit_joins.lua"
    "CapitalEnter" = "_ai/100_ai_capital.lua"
    "EnterGreen2" = "_features/105_emerald_dream.lua"
    "Unit Item Tables" = "_features/110_item_drops.lua"
    "Sound Assets" = "_features/115_sounds.lua"
    "Unit Creation" = "_data/120_unit_creation.lua"
    "Regions" = "_data/130_regions.lua"
    "Cameras" = "_data/135_cameras.lua"
    "Triggers" = "triggers/__triggers_full__.lua"
}

# Find section starts
$sections = @()
$currentName = "__header"
$currentStart = 0

for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match '^-- \*\s{2,3}(\S.*?)$') {
        $sname = $Matches[1].Trim()
        if ($sectionMap.Contains($sname)) {
            if ($currentStart -le $i - 1) {
                $sections += @{ Name = $currentName; Start = $currentStart; End = $i - 1 }
            }
            $currentName = $sname
            $currentStart = $i
        }
    }
}
if ($currentStart -le $lines.Count - 1) {
    $sections += @{ Name = $currentName; Start = $currentStart; End = $lines.Count - 1 }
}

# Write all non-"Triggers" sections
Write-Host "Writing non-trigger files..."
$sectionFileMap = @{ "__header" = "_infra/00_header.lua" }
foreach ($k in $sectionMap.Keys) { $sectionFileMap[$k] = $sectionMap[$k] }

foreach ($sec in $sections) {
    $fname = $sectionFileMap[$sec.Name]
    if ($fname -eq $null) {
        Write-Host "WARNING: no mapping for section '$($sec.Name)'"
        continue
    }
    $arr = $lines[$sec.Start..$sec.End]
    Write-LuaFile $fname $arr
    Write-Host "  $fname ($($arr.Count) lines)"
}

# ── split triggers ──
Write-Host "Splitting triggers..."
$triggerSplits = @(
    ("InitTrig_Demontag",               "triggers/01_core_economy.lua"),
    ("InitTrig_FastResearch",           "triggers/02_game_modes.lua"),
    ("InitTrig_DisIncomeStart",         "triggers/03_continents_diplomacy.lua"),
    ("InitTrig_Page4",                  "triggers/04_race_selection.lua"),
    ("InitTrig_Aura_Flagmana_Stoikost_O","triggers/05_common_spells.lua"),
    ("InitTrig_MageTpSell",             "triggers/06_transport_portals.lua"),
    ("InitTrig_Duel",                   "triggers/07_hero_bezlikie_horde.lua"),
    ("InitTrig_TrainHakkar",            "triggers/08_undead_trolls.lua"),
    ("InitTrig_StartAlliance",          "triggers/09_alliance.lua"),
    ("InitTrig_Klap_Klap_War_big",      "triggers/10_forsaken_gnomes.lua"),
    ("InitTrig_StartHorde",             "triggers/11_horde.lua"),
    ("InitTrig_AreaOfDeath2",           "triggers/12_silitid_goblin_bloodelf_bandit.lua"),
    ("InitTrig_TrainGreenSpellSteal",   "triggers/13_subraces_nightelf_naga_illidari_dragon.lua"),
    ("InitTrig_QoggSpawn",              "triggers/14_demon_elemental_undead_boss.lua"),
    ("InitTrig_DalIn_Copy",             "triggers/15_ai_portals_cities.lua")
)

# Read the single triggers file
$trigFilePath = Join-Path $outDir "triggers/__triggers_full__.lua"
$trigLines = Get-Content -LiteralPath $trigFilePath -Encoding UTF8
$trigTotal = $trigLines.Count

$initLines = @{}
for ($i = 0; $i -lt $trigTotal; $i++) {
    if ($trigLines[$i] -match '^function InitTrig_(\w+)\(\)') {
        $initLines[$Matches[1]] = $i + 1
    }
}

$prevStart = 1
for ($si = 0; $si -lt $triggerSplits.Count; $si++) {
    $split = $triggerSplits[$si]
    $initName = $split[0]
    $fileName = $split[1]
    $key = $initName.Replace("InitTrig_", "")
    $endLine = $initLines[$key]
    if ($endLine -eq $null) { Write-Host "ERROR: $initName not found"; exit 1 }
    
    # Last file goes to end of triggers
    $isLast = ($si -eq $triggerSplits.Count - 1)
    if ($isLast) { $endLine = $trigTotal }
    
    $arr = $trigLines[($prevStart-1)..($endLine-1)]
    Write-LuaFile $fileName $arr
    Write-Host ("  $fileName : $prevStart-$endLine ($($arr.Count) lines)")
    $prevStart = $endLine + 1
}

# Remove temp full triggers file
Remove-Item -LiteralPath $trigFilePath -Force

# ── collect all output files in order ──
function Get-SortedFiles($dir, $base) {
    $result = @()
    foreach ($f in (Get-ChildItem -LiteralPath $dir -File -Name | Sort-Object)) {
        $result += "$base/$f"
    }
    foreach ($d in (Get-ChildItem -LiteralPath $dir -Directory -Name | Sort-Object)) {
        $result += Get-SortedFiles (Join-Path $dir $d) "$base/$d"
    }
    return $result
}

# Build ordered file list from section writing order
$orderedFiles = @()
foreach ($sec in $sections) {
    $fkey = $sec.Name
    $fname = $sectionFileMap[$fkey]
    if ($fname -eq $null) { continue }
    if ($sec.Name -eq "Triggers") { continue }  # triggers handled separately
    
    # Determine which directory and filename
    $orderedFiles += $fname
}

# Add trigger files in their split order
foreach ($split in $triggerSplits) {
    $orderedFiles += $split[1]
}

# Verify we captured all files
$allFilesCheck = @{}
foreach ($f in $orderedFiles) { $allFilesCheck[$f] = $true }
foreach ($d in $dirOrder) {
    foreach ($f in (Get-ChildItem -LiteralPath (Join-Path $outDir $d) -File -Name | Sort-Object)) {
        $r = "$d/$f"
        if (-not $allFilesCheck[$r]) {
            Write-Host "WARNING: file not in order: $r"
        }
    }
}

# ── verify ──
Write-Host ""
Write-Host "Verifying rebuild..."
$assembled = [System.Collections.Generic.List[byte]]::new()
foreach ($f in $orderedFiles) {
    $fb = [System.IO.File]::ReadAllBytes((Join-Path $outDir $f))
    $assembled.AddRange($fb)
}

if ($assembled.Count -ne $sourceBytes.Count) {
    Write-Host "ERROR: Byte mismatch! Orig=$($sourceBytes.Count) Built=$($assembled.Count) Diff=$($assembled.Count - $sourceBytes.Count)"
    exit 1
}
for ($i = 0; $i -lt $sourceBytes.Count; $i++) {
    if ($assembled[$i] -ne $sourceBytes[$i]) {
        Write-Host "ERROR: First diff at byte $i"
        exit 1
    }
}
Write-Host "OK: Rebuild matches byte-for-byte ($($assembled.Count) bytes)"

# ── update manifest ──
Write-Host "Updating manifest.json..."
$manifestRaw = Get-Content -LiteralPath $manifestPath -Encoding UTF8 -Raw
$manifest = $manifestRaw | ConvertFrom-Json

$genIdx = $null
for ($i = 0; $i -lt $manifest.sections.Count; $i++) {
    if ($manifest.sections[$i].name -eq "generated_runtime") {
        $genIdx = $i
        break
    }
}

$newEntries = @()
foreach ($f in $orderedFiles) {
    $newEntries += @{
        name = "gen:" + ($f -replace '/','_')
        file = "80_runtime/$f"
        category = "generated_runtime"
        start_line = 0
        end_line = 0
        library_name = $null
    }
}

$manifest.sections = $manifest.sections[0..($genIdx-1)] + $newEntries + $manifest.sections[($genIdx+1)..($manifest.sections.Count-1)]
$manifest.section_count = $manifest.sections.Count

# Write manifest using ConvertTo-Json for proper escaping
$newJson = $manifest | ConvertTo-Json -Depth 4
[System.IO.File]::WriteAllText($manifestPath, $newJson, $encoding)

Write-Host ""
Write-Host "DONE: $($orderedFiles.Count) files in 80_runtime/"
Write-Host "Run: python build_map_lua.py --check-only"
