# Audit qualité des données Bitvavo

Scan : 2026-09-19T08:00:11.153389+00:00 (20260919T075809Z-2b80b0d1)
Univers : 427 | strategy-grade : 33 | rejetés : 394
5m valides : 39 | 15m valides : 67 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 388 |
| INVALID_15M | 360 |
| MISSING_LATEST_CLOSED_CANDLE | 204 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 388 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 360 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 4932484 | +4.34% | INVALID_5M | 100/2 | 100/0 |
| USELESS-EUR | 1995038 | +5.22% | INVALID_5M | 100/2 | 100/0 |
| POL-EUR | 1656380 | +2.98% | INVALID_5M | 99/2 | 100/0 |
| APT-EUR | 1628492 | +4.67% | INVALID_5M | 100/1 | 100/0 |
| CNPY-EUR | 1594842 | +10.86% | INVALID_5M | 99/1 | 100/0 |
| F-EUR | 1574429 | +31.87% | INVALID_5M | 100/1 | 94/0 |
| SKY-EUR | 1420261 | +15.21% | INVALID_5M | 99/5 | 100/0 |
| HBAR-EUR | 1213668 | +2.19% | INVALID_15M, INVALID_5M | 99/1 | 100/1 |
| AAVE-EUR | 1111634 | +6.04% | INVALID_5M | 100/1 | 100/0 |
| OP-EUR | 1102295 | +11.82% | INVALID_5M | 99/3 | 100/0 |
| RAY-EUR | 1097198 | +4.82% | INVALID_15M, INVALID_5M | 99/3 | 100/1 |
| BCH-EUR | 1023924 | -1.68% | INVALID_15M, INVALID_5M | 100/2 | 100/2 |
| COTI-EUR | 961024 | -11.25% | INVALID_15M | 100/0 | 100/2 |
| LPT-EUR | 914969 | +7.78% | INVALID_5M | 100/5 | 100/0 |
| SAGA-EUR | 911931 | +18.46% | INVALID_5M | 99/5 | 100/0 |
| BNB-EUR | 850407 | +0.79% | INVALID_15M, INVALID_5M | 100/6 | 100/1 |
| MORPHO-EUR | 841439 | +13.33% | INVALID_15M, INVALID_5M | 99/1 | 100/1 |
| S-EUR | 833478 | +8.26% | INVALID_5M | 100/7 | 100/0 |
| XPL-EUR | 827040 | +0.26% | INVALID_15M, INVALID_5M | 100/15 | 100/2 |
| TIA-EUR | 807258 | +1.66% | INVALID_5M | 100/7 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
