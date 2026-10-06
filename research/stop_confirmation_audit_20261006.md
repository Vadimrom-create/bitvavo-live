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
| close_5m | 88 | 4 | 11 | 0.15583 | -0.32642 |
| close_2x5m | 77 | 7 | 22 | 0.24775 | -0.50596 |
| close_15m | 80 | 7 | 19 | 0.18104 | -0.43042 |

## Hard-stop sensitivity

| Hard stop | Hits | Not hit |
|---|---:|---:|
| 1.25R | 58 | 41 |
| 1.5R | 38 | 61 |
| 1.75R | 21 | 78 |

## Manual reference cases

- **VTHO_2026-10-06 / VTHO-EUR**: stop 0.00064761, touch low 0.00064332, actual exit 0.000634, 15m vs stop -1.3928%, 60m vs stop 0.6547%, 4h vs stop 2.2483%.

## Limits

- 5m OHLC data cannot reveal the exact intrabar path.
- Confirmation policies are diagnostic only; they intentionally ignore profit-taking to isolate stop behaviour.
- The 1.50R catastrophe stop is a research candidate, not a live recommendation.
- BUY_SENT entries are Solaire recommendations, not necessarily every manually executed account trade.
