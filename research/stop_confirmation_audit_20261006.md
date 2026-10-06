# Stop confirmation audit — 2026-10-06

Research-only: no production rule was changed.

- Stop-touch cases analysed: **99**
- Wick reclaims within 15m: **23**
- Back above stop after 60m: **58**
- Back above stop after 4h: **47**

## Policy comparison

| Policy | Exits | Hard-stop exits | Held to 4h | Mean delta vs touch (pp) | Median delta (pp) |
|---|---:|---:|---:|---:|---:|
| touch | 99 | 0 | 0 | 0.0 | 0.0 |
| close_5m | 88 | 4 | 11 | 0.14862 | -0.32642 |
| close_2x5m | 77 | 8 | 22 | 0.23494 | -0.50596 |
| close_15m | 80 | 8 | 19 | 0.16824 | -0.43042 |

## Hard-stop sensitivity

| Hard stop | Hits | Not hit |
|---|---:|---:|
| 1.25R | 58 | 41 |
| 1.5R | 38 | 61 |
| 1.75R | 21 | 78 |

## Confirmation × hard-stop matrix

| Hard stop | Policy | Improved | Worsened | Held 4h | Hard exits | Mean delta (pp) | Median delta (pp) | Worst (pp) | Best (pp) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.25R | close_5m | 9 | 90 | 9 | 22 | -0.03533 | -0.34426 | -2.4839 | 13.25369 |
| 1.25R | close_2x5m | 18 | 81 | 20 | 28 | 0.01931 | -0.60966 | -2.4839 | 13.25369 |
| 1.25R | close_15m | 16 | 83 | 17 | 28 | -0.00655 | -0.49767 | -2.4839 | 13.25369 |
| 1.5R | close_5m | 11 | 88 | 11 | 4 | 0.14862 | -0.32642 | -3.8145 | 13.25369 |
| 1.5R | close_2x5m | 20 | 79 | 22 | 8 | 0.23494 | -0.50596 | -3.8145 | 13.25369 |
| 1.5R | close_15m | 18 | 81 | 19 | 8 | 0.16824 | -0.43042 | -3.8145 | 13.25369 |
| 1.75R | close_5m | 12 | 87 | 12 | 0 | 0.65406 | -0.29659 | -2.38357 | 39.24828 |
| 1.75R | close_2x5m | 21 | 78 | 23 | 0 | 0.74538 | -0.44459 | -3.28257 | 39.24828 |
| 1.75R | close_15m | 19 | 80 | 20 | 1 | 0.66665 | -0.36804 | -4.49745 | 39.24828 |

## Manual reference cases

- **VTHO_2026-10-06 / VTHO-EUR**: stop 0.00064761, touch low 0.00063722, actual exit 0.000634, 15m vs stop -1.4453%, 60m vs stop 0.3799%, 4h vs stop 1.7603%.

## Limits

- 5m OHLC data cannot reveal the exact intrabar path.
- Confirmation policies are diagnostic only; they intentionally ignore profit-taking to isolate stop behaviour.
- The 1.50R catastrophe stop is a research candidate, not a live recommendation.
- BUY_SENT entries are Solaire recommendations, not necessarily every manually executed account trade.
