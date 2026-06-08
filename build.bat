@echo off
REM Rebuild map.w3x/war3map.lua from the split sources, then syntax-check it.
REM Double-click or run from a terminal. Edits go in _lua/monolith_split/sections/.
setlocal
cd /d "%~dp0"

echo [build] rebuilding war3map.lua from split sources...
python build_map_lua.py
if errorlevel 1 goto :err

echo [build] luaparser syntax check...
python -c "import luaparser.ast as a; a.parse(open(r'map.w3x/war3map.lua',encoding='utf-8').read()); print('LUA OK')"
if errorlevel 1 goto :err

echo.
echo [build] OK
goto :end

:err
echo.
echo [build] FAILED
:end
pause
