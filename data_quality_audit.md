# Audit qualité des données Bitvavo

Scan : 2026-09-19T14:34:16.653836+00:00 (20260919T143215Z-1b9d8ce3)
Univers : 427 | strategy-grade : 33 | rejetés : 394
5m valides : 35 | 15m valides : 82 | deux intervalles valides : 34

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 345 |
| MISSING_LATEST_CLOSED_CANDLE | 259 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 345 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 2971944 | +2.84% | INVALID_5M | 99/1 | 99/0 |
| G-EUR | 2389670 | -12.91% | INVALID_5M | 99/1 | 99/0 |
| ARB-EUR | 2098309 | -0.23% | INVALID_5M | 99/1 | 99/0 |
| LSK-EUR | 1945512 | -6.91% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1793747 | +8.20% | INVALID_5M | 99/3 | 99/0 |
| POL-EUR | 1622300 | +5.32% | INVALID_5M | 99/3 | 99/0 |
| CAP-EUR | 1375571 | -25.14% | INVALID_15M | 79/0 | 99/2 |
| SAGA-EUR | 1328640 | +27.63% | INVALID_5M | 99/1 | 99/0 |
| SKY-EUR | 1321217 | -0.30% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/8 | 100/0 |
| OP-EUR | 1196527 | +12.05% | INVALID_5M | 99/4 | 100/0 |
| AAVE-EUR | 1108402 | +4.49% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 979333 | -1.07% | INVALID_5M | 99/3 | 99/0 |
| BCH-EUR | 913004 | -0.02% | INVALID_5M | 99/7 | 99/0 |
| C-EUR | 867324 | +18.48% | INVALID_5M | 99/4 | 99/0 |
| HEI-EUR | 862248 | +17.03% | INVALID_5M | 99/3 | 99/0 |
| RAY-EUR | 821866 | +7.51% | INVALID_5M | 100/1 | 100/0 |
| MORPHO-EUR | 801788 | +11.63% | INVALID_5M | 99/6 | 99/0 |
| COTI-EUR | 765069 | -2.01% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 100/0 |
| JUP-EUR | 760369 | +8.82% | INVALID_5M | 99/3 | 99/0 |
| EPIC-EUR | 750569 | +19.34% | INVALID_5M | 100/5 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
