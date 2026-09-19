# Audit qualité des données Bitvavo

Scan : 2026-09-19T17:21:16.615207+00:00 (20260919T171952Z-c794557e)
Univers : 427 | strategy-grade : 35 | rejetés : 392
5m valides : 38 | 15m valides : 89 | deux intervalles valides : 36

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 389 |
| INVALID_15M | 338 |
| MISSING_LATEST_CLOSED_CANDLE | 232 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 389 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 338 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| STRK-EUR | 2180046 | +17.52% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1857586 | +6.71% | INVALID_5M | 100/2 | 99/0 |
| CAP-EUR | 1826119 | -16.33% | INVALID_15M | 99/0 | 99/2 |
| POL-EUR | 1546086 | +3.91% | INVALID_5M | 99/3 | 99/0 |
| LTC-EUR | 1511346 | +3.26% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1420568 | +4.59% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 1416433 | +5.01% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1216344 | +8.84% | INVALID_5M | 99/8 | 99/0 |
| VET-EUR | 1104301 | +10.90% | INVALID_5M | 99/1 | 99/0 |
| F-EUR | 1101917 | -15.34% | INVALID_5M | 100/5 | 99/0 |
| SKY-EUR | 1050065 | +1.05% | INVALID_15M, INVALID_5M | 99/6 | 99/1 |
| DOT-EUR | 946139 | +0.56% | INVALID_5M | 100/2 | 99/0 |
| BCH-EUR | 933701 | +3.14% | INVALID_5M | 99/4 | 99/0 |
| AAVE-EUR | 910779 | +3.80% | INVALID_5M | 99/7 | 99/0 |
| COTI-EUR | 907334 | -1.05% | INVALID_5M | 99/1 | 99/0 |
| KAS-EUR | 807426 | +9.48% | INVALID_5M | 99/1 | 99/0 |
| MORPHO-EUR | 802575 | +11.93% | INVALID_5M | 100/3 | 99/0 |
| HEI-EUR | 779703 | +12.79% | INVALID_5M | 100/3 | 99/0 |
| JUP-EUR | 744500 | +6.74% | INVALID_5M | 100/7 | 99/0 |
| RAY-EUR | 662645 | +3.22% | MISSING_LATEST_CLOSED_CANDLE | 100/0 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
