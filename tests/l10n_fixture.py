"""Loc() for tests that execute single sections: the generated 03_localization.lua with a fixed client locale."""
from pathlib import Path

LOCALIZATION = (Path(__file__).resolve().parents[1] /
                'map.w3x/_lua/monolith_split/sections/03_localization.lua').read_text(encoding='utf-8')


def install_loc(lua, locale='ruRU'):
    """Define Loc() as the real map does; tests assert Russian source texts by default."""
    lua.execute(f'BlzGetLocale = BlzGetLocale or function() return "{locale}" end')
    # Hide timer natives so the first-tick locale re-check does not show up in fixture handle counts.
    lua.execute('__l10n_timers = {TimerStart, CreateTimer}; TimerStart = nil; CreateTimer = nil')
    lua.execute(LOCALIZATION)
    lua.execute('TimerStart, CreateTimer = __l10n_timers[1], __l10n_timers[2]; __l10n_timers = nil')
