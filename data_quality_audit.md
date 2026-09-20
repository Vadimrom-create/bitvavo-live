# Audit qualité des données Bitvavo

Scan : 2026-09-20T03:14:07.309180+00:00 (20260920T031206Z-241630ee)
Univers : 427 | strategy-grade : 28 | rejetés : 399
5m valides : 30 | 15m valides : 57 | deux intervalles valides : 28

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 397 |
| INVALID_15M | 370 |
| MISSING_LATEST_CLOSED_CANDLE | 203 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 397 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 370 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| NEAR-EUR | 5824975 | -7.78% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2778644 | -2.49% | INVALID_5M | 99/2 | 99/0 |
| SYN-EUR | 2316380 | +11.73% | INVALID_5M | 99/1 | 99/0 |
| UNI-EUR | 2048690 | -5.07% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 2003229 | -15.95% | INVALID_5M | 100/8 | 99/0 |
| PUMP-EUR | 1961421 | -8.33% | INVALID_5M | 99/5 | 99/0 |
| DOGE-EUR | 1644642 | -2.91% | INVALID_5M | 99/3 | 99/0 |
| CNPY-EUR | 1461143 | -26.21% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1427381 | -2.82% | INVALID_5M | 99/9 | 99/0 |
| VET-EUR | 1344049 | +6.55% | INVALID_5M | 99/3 | 99/0 |
| APT-EUR | 1277482 | -5.69% | INVALID_15M, INVALID_5M | 99/9 | 99/2 |
| EPIC-EUR | 1209496 | +12.19% | INVALID_15M, INVALID_5M | 99/14 | 99/3 |
| STRK-EUR | 1192634 | +1.96% | INVALID_5M | 99/2 | 99/0 |
| USELESS-EUR | 1092443 | -15.67% | INVALID_5M | 99/3 | 99/0 |
| ARB-EUR | 1084615 | -4.22% | INVALID_5M | 99/2 | 99/0 |
| OP-EUR | 974605 | -1.67% | INVALID_15M, INVALID_5M | 99/19 | 99/4 |
| FIL-EUR | 926496 | -2.08% | INVALID_15M, INVALID_5M | 100/15 | 99/1 |
| STX-EUR | 918086 | +9.00% | INVALID_5M | 99/2 | 99/0 |
| HEI-EUR | 893236 | +12.37% | INVALID_15M, INVALID_5M | 99/17 | 99/2 |
| BCH-EUR | 851632 | -4.30% | INVALID_15M, INVALID_5M | 97/28 | 99/4 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
