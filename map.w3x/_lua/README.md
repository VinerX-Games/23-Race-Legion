# Lua Source Layout

- Canonical runtime source: `map.w3x/_lua/monolith_split/`
- Canonical built script: `map.w3x/war3map.lua`
- Canonical rebuild command:

```bash
python build_map_lua.py
```

## Rules

- Edit the split source files, not `war3map.lua` directly.
- Rebuild `war3map.lua` after every intentional Lua change.
- Keep the split tree exact and reproducible first; semantic refactoring happens on top of that baseline.
