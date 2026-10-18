@echo off
"F:\WARCRAFT III\WARCRAFT_SOFT\HiveWE\HiveWE_cli.exe" probe-map --map "F:\Gemini_23Race\map.w3x" --warcraft "F:\Games\Warcraft III" --args "-window -nowfpause" --click-after 60 --wait 360 --bridge-script "140:create_ai:2" --probe-log "23Race_probe_log.pld" --keep-open %*
