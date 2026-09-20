# Audit qualité des données Bitvavo

Scan : 2026-09-20T05:27:44.479186+00:00 (20260920T052544Z-ff1c61f9)
Univers : 427 | strategy-grade : 23 | rejetés : 404
5m valides : 24 | 15m valides : 59 | deux intervalles valides : 24

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 403 |
| INVALID_15M | 368 |
| MISSING_LATEST_CLOSED_CANDLE | 300 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 403 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 368 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| ONDO-EUR | 6084013 | +0.76% | INVALID_5M | 99/2 | 99/0 |
| INJ-EUR | 3185148 | +8.91% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2792029 | -2.80% | INVALID_5M | 99/1 | 99/0 |
| SYN-EUR | 2299323 | +6.75% | INVALID_5M | 99/2 | 99/0 |
| HBAR-EUR | 2106884 | +1.88% | INVALID_5M | 99/6 | 99/0 |
| FET-EUR | 2082337 | -5.62% | INVALID_5M | 99/1 | 99/0 |
| CAP-EUR | 1999530 | -17.63% | INVALID_5M | 100/8 | 99/0 |
| PUMP-EUR | 1969747 | -3.77% | INVALID_5M | 99/2 | 99/0 |
| DOGE-EUR | 1651352 | -3.00% | INVALID_5M | 99/4 | 99/0 |
| LSK-EUR | 1514123 | -9.98% | INVALID_5M | 99/2 | 99/0 |
| CNPY-EUR | 1487215 | -28.03% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1416269 | -2.25% | INVALID_5M | 99/3 | 99/0 |
| WLD-EUR | 1375363 | -0.02% | INVALID_5M | 99/1 | 99/0 |
| EPIC-EUR | 1202936 | +10.18% | INVALID_15M, INVALID_5M | 100/1 | 99/3 |
| VET-EUR | 1191107 | +0.66% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 1167109 | -6.35% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/13 | 100/2 |
| STRK-EUR | 1075088 | +13.34% | MISSING_LATEST_CLOSED_CANDLE | 100/0 | 99/0 |
| USELESS-EUR | 1014586 | -8.63% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 946824 | +13.40% | INVALID_5M | 99/2 | 99/0 |
| FIL-EUR | 909433 | -2.78% | INVALID_15M, INVALID_5M | 99/18 | 99/3 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
