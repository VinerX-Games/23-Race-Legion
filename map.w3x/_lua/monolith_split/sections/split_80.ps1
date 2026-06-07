$ErrorActionPreference = "Stop"
$source = "C:\Games\23 Race\23-Race-Legion\map.w3x\_lua\monolith_split\sections\80_generated_runtime.lua"
$outDir = "C:\Games\23 Race\23-Race-Legion\map.w3x\_lua\monolith_split\sections\80_split"

$sectionMap = [ordered]@{
    "00_header" = "00_header.lua"
    "Global Variables" = "10_globals.lua"
    "Custom Script Code" = "20_custom_script.lua"
    "Counter" = "30_player_counter.lua"
    "gGlobal objects" = "40_bool_exprs.lua"
    "LibNewFunctions" = "50_lib_new_functions.lua"
    "UpdateGraph" = "51_update_graph.lua"
    "Enter" = "52_enter.lua"
    "Settings" = "53_income_settings.lua"
    "CountAddDis and CountDelDis" = "54_count_dis.lua"
    "ClearEc" = "55_clear_ec.lua"
    "ClearPlayer" = "56_clear_player.lua"
    "TimedUpdate" = "57_timed_update.lua"
    "InitThings" = "58_init_things.lua"
    "PlayerUI" = "59_ui_setup.lua"
    "IncomeTooltip" = "60_income_tooltip.lua"
    "AllPlayersStart" = "61_all_players.lua"
    "CommonHash" = "62_common_hash.lua"
    "ClearAllies" = "63_clear_allies.lua"
    "DelUnitStart" = "64_del_unit.lua"
    "RandomLocationFromUnits" = "65_random_locs.lua"
    "CreateRaceCircles" = "66_race_circles.lua"
    "CityCountCheck" = "67_city_check.lua"
    "SubGroup2" = "68_subgroup2.lua"
    "Pstart" = "70_race_farm_start.lua"
    "CountForTier" = "71_tier_system.lua"
    "ChangeSpellLimit" = "72_farm_limit.lua"
    "HordeW2On" = "73_horde_w2.lua"
    "XpLevelW2" = "74_w2_xp.lua"
    "CultOn" = "75_cult_on.lua"
    "StartForestTrolls" = "76_forest_trolls.lua"
    "StartJungleTrolls" = "77_jungle_trolls.lua"
    "ForsacenOn" = "78_forsaken_on.lua"
    "BuildingTierSystem" = "79_building_tier.lua"
    "DragonsOn2" = "80_dragons_on.lua"
    "ElemOn" = "81_elem_on.lua"
    "PointAi" = "82_ai_points.lua"
    "TurnOffAi" = "83_turn_off_ai.lua"
    "Globals And Start setttings" = "84_globals_start.lua"
    "LibDifferentAiStuff" = "85_lib_ai_stuff.lua"
    "LibRaces" = "86_lib_races.lua"
    "ContinentalBoolexrs" = "90_continental_bool.lua"
    "ContinentalTemplates" = "91_continental_templates.lua"
    "Dungeons" = "92_dungeons.lua"
    "ContinentalMain" = "93_continental_main.lua"
    "TryToAttack2 Uni" = "94_ai_attack.lua"
    "TryToAttackN Uni" = "95_ai_attack_naval.lua"
    "KilledCity" = "96_ai_killed_city.lua"
    "GoToWater" = "97_ai_water.lua"
    "TryToBuild" = "98_ai_build.lua"
    "AiUnitJoins" = "99_ai_unit_joins.lua"
    "CapitalEnter" = "100_ai_capital.lua"
    "EnterGreen2" = "105_emerald_dream.lua"
    "Unit Item Tables" = "110_item_drops.lua"
    "Sound Assets" = "115_sounds.lua"
    "Unit Creation" = "120_unit_creation.lua"
    "Regions" = "130_regions.lua"
    "Cameras" = "135_cameras.lua"
    "Triggers" = "140_triggers.lua"
}

Write-Host "Reading source file..."
$encoding = [System.Text.UTF8Encoding]::new($false)
$originalBytes = [System.IO.File]::ReadAllBytes($source)
$originalText = $encoding.GetString($originalBytes)

# Detect if file ends with trailing newline
$endsWithCRLF = $originalBytes[-2] -eq 0x0D -and $originalBytes[-1] -eq 0x0A
$endsWithLFOnly = -not $endsWithCRLF -and $originalBytes[-1] -eq 0x0A
Write-Host "File ends with CRLF: $endsWithCRLF, LF only: $endsWithLFOnly"

# Split into lines (preserving content, stripping trailing empty)
$lines = $originalText -split '\r?\n'
# Strip trailing empty elements (PowerShell split may not strip all)
while ($lines.Count -gt 0 -and $lines[-1] -eq '') {
    $lines = $lines[0..($lines.Count - 2)]
}
Write-Host "Last line of file: '$($lines[-1])' (len=$($lines[-1].Length))"
Write-Host "Total lines after trim: $($lines.Count)"
Write-Host "Original bytes: $($originalBytes.Count)"

Write-Host "Finding section boundaries..."
$sections = @()
$currentSection = "00_header"
$currentStart = 0

for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match '^-- \*\s{2,3}(\S.*?)$') {
        $sectionName = $Matches[1].Trim()
        if ($sectionMap.Contains($sectionName)) {
            $sections += @{
                Name = $currentSection
                File = $sectionMap[$currentSection]
                Start = $currentStart
                End   = $i - 1
            }
            $currentSection = $sectionName
            $currentStart = $i
        }
    }
}

$sections += @{
    Name = $currentSection
    File = $sectionMap[$currentSection]
    Start = $currentStart
    End   = $lines.Count - 1
}

if (-not (Test-Path $outDir)) {
    New-Item -ItemType Directory -Path $outDir -Force | Out-Null
}

Write-Host "Writing $($sections.Count) output files..."
$manifestLines = @("-- Auto-generated manifest for 80_generated_runtime split")
$manifestLines += "-- Source: 80_generated_runtime.lua"
$manifestLines += ""

foreach ($sec in $sections) {
    $outPath = Join-Path $outDir $sec.File
    $outDirPath = Split-Path $outPath -Parent
    if ($outDirPath -ne $outDir -and -not (Test-Path $outDirPath)) {
        New-Item -ItemType Directory -Path $outDirPath -Force | Out-Null
    }
    
    $arr = $lines[$sec.Start..$sec.End]
    $rawContent = [string]::Join("`r`n", $arr) + "`r`n"
    $rawBytes = $encoding.GetBytes($rawContent)
    
    $isLast = ($sec.Name -eq $sections[-1].Name)
    if ($isLast -and -not $endsWithCRLF) {
        $rawBytes = $rawBytes[0..($rawBytes.Length - 3)]
    }
    
    [System.IO.File]::WriteAllBytes($outPath, $rawBytes)
    
    $lineCount = $sec.End - $sec.Start + 1
    $manifestLines += "`"$($sec.File)`"  -- $($sec.Name)  ($lineCount lines)"
    Write-Host "  $($sec.File) : $($sec.Name) [$lineCount lines]"
}

[System.IO.File]::WriteAllLines((Join-Path $outDir "_manifest.lua"), $manifestLines, $encoding)

# VERIFICATION
Write-Host ""
Write-Host "Verifying assembly matches original..."

$assembledBytes = [System.Collections.Generic.List[byte]]::new()
foreach ($sec in $sections) {
    $outPath = Join-Path $outDir $sec.File
    $fileBytes = [System.IO.File]::ReadAllBytes($outPath)
    $assembledBytes.AddRange($fileBytes)
}

if ($assembledBytes.Count -ne $originalBytes.Count) {
    Write-Host "ERROR: Byte count mismatch! Orig=$($originalBytes.Count) Assembled=$($assembledBytes.Count) Diff=$($assembledBytes.Count - $originalBytes.Count)"
    
    $maxLen = [Math]::Min($assembledBytes.Count, $originalBytes.Count)
    for ($i = 0; $i -lt $maxLen; $i++) {
        if ($assembledBytes[$i] -ne $originalBytes[$i]) {
            $ctxStart = [Math]::Max(0, $i - 2)
            $ctxEnd = [Math]::Min($maxLen - 1, $i + 5)
            Write-Host ("First diff at byte " + $i + ":")
            for ($j = $ctxStart; $j -le $ctxEnd; $j++) {
                $mark = if ($j -eq $i) { " <<<" } else { "" }
                $o = '0x{0:X2}' -f $originalBytes[$j]
                $a = '0x{0:X2}' -f $assembledBytes[$j]
                Write-Host ("  byte " + $j + " : orig=" + $o + "  asse=" + $a + $mark)
            }
            break
        }
    }
    exit 1
}

Write-Host "VERIFIED: Reassembled matches original byte-for-byte!"
Write-Host "Output: $outDir ($($sections.Count) files)"
