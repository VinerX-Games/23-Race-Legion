# Portal Graph

Собрано `ai_portal_graph_probe.lua`. 73 портала (n003, n006, n01D, n01Y, n01Z). Водные порталы n01D исключены (пролив флота).

## Рёбра (continent → continent)

```
Ankirag         ↔ Kalimdor          ×2
Argus           ↔ BrokenIsles       ×1
Argus           → Kalimdor          ×1
Azgel           → Kalimdor          ×1
Azgel           ↔ Northrend         ×2
BlackMountain   ↔ EasternKingdoms   ×2
DeadMines       ↔ EasternKingdoms   ×2
EasternDungeons ↔ EasternKingdoms   ×2
EasternKingdoms → BrokenIsles       ×1
EasternKingdoms → Kalimdor          ×1
EasternKingdoms ↔ Outland           ×2
EasternKingdoms → Uldum             ×3
EasternKingdoms ↔ Undercity         ×2
EmeraldDream    → ?                 ×5  (dst=(-30688,-30688) — не задан)
Kalimdor        → Argus             ×1
Kalimdor        → Azgel             ×1
Kalimdor        → Outland           ×1
Kalimdor        ↔ Ankirag           ×2
Kalimdor        ↔ Maradon           ×2
Kalimdor        ↔ Orgrimmar         ×2
Maradon         ↔ Kalimdor          ×2
Naxramas        → Northrend         ×1
Northrend       ↔ Azgel             ×2
Northrend       ↔ Northrend         ×1  (внутренний)
Orgrimmar       ↔ Kalimdor          ×2
Outland         → EasternKingdoms   ×2
Outland         → Kalimdor          ×1
Uldum           → EasternKingdoms   ×3
Undercity       → EasternKingdoms   ×2
EasternKingdoms → EasternKingdoms   ×4  (внутренние EK)
Kalimdor        → Kalimdor          ×2  (внутренние Kalimdor)
```

## Непокрытые rect'ами (2+11)

| Тип    | Координаты src          | Координаты dst          | Примечание                     |
|--------|------------------------|------------------------|--------------------------------|
| n003   | (-12096, -21632)       | ?                      | чуть севернее EasternDungeons  |
| n01Y×8 | EmeraldDream           | (-30688, -30688)       | waygate не задан               |
| n01Z×2 | ? / BrokenIsles        | (-30688, -30688)       | waygate не задан               |
| n01D×2 | (30464,14464)↔(30400,20288) |                  | водные, исключены              |

## Легенда континентов

| Континент         | Rect                     |
|-------------------|--------------------------|
| Kalimdor          | gg_rct_Kalim             |
| EasternKingdoms   | gg_rct_EastenKingdoms    |
| Northrend         | gg_rct_Nord              |
| Pandaria          | gg_rct_Pandaria          |
| Outland           | gg_rct_Outland           |
| BrokenIsles       | gg_rct_BrokenIsles       |
| Argus             | gg_rct_Argus             |
| Azgel             | gg_rct_Azgel             |
| Ankirag           | gg_rct_Ankirag           |
| BlackMountain     | gg_rct_BlackMountain     |
| Orgrimmar         | gg_rct_Orgrimmar         |
| Uldum             | gg_rct_Uldum             |
| Undercity         | gg_rct_Undercity         |
| Maradon           | gg_rct_Maradon           |
| DeadMines         | gg_rct_DeadMines         |
| Naxramas          | gg_rct_Naxramas          |
| EasternDungeons   | gg_rct_EasternDungeons   |
| EmeraldDream      | gg_rct_EmeraldDream      |
