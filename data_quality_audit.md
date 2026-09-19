# Audit qualité des données Bitvavo

Scan : 2026-09-19T19:50:19.912998+00:00 (20260919T194844Z-465730ff)
Univers : 427 | strategy-grade : 35 | rejetés : 392
5m valides : 35 | 15m valides : 93 | deux intervalles valides : 35

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 334 |
| MISSING_LATEST_CLOSED_CANDLE | 241 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 334 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| CAP-EUR | 1980377 | -13.02% | INVALID_5M | 100/1 | 99/0 |
| STRK-EUR | 1921770 | +3.12% | INVALID_5M | 99/3 | 99/0 |
| PUMP-EUR | 1811697 | -6.07% | INVALID_5M | 99/4 | 99/0 |
| APT-EUR | 1795433 | +5.57% | INVALID_5M | 100/6 | 99/0 |
| ARB-EUR | 1686291 | -5.72% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1508335 | +1.59% | INVALID_5M | 99/2 | 99/0 |
| POL-EUR | 1333485 | -1.94% | INVALID_5M | 100/4 | 99/0 |
| OP-EUR | 1229210 | +6.37% | INVALID_5M | 99/9 | 99/0 |
| SKY-EUR | 1047472 | -1.57% | INVALID_15M, INVALID_5M | 100/20 | 100/3 |
| BCH-EUR | 981641 | +0.50% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/4 | 100/0 |
| DOT-EUR | 942388 | -0.17% | INVALID_5M | 100/2 | 99/0 |
| AAVE-EUR | 901078 | +2.80% | INVALID_5M | 99/4 | 100/0 |
| SAGA-EUR | 889516 | -1.36% | INVALID_5M | 100/6 | 99/0 |
| COTI-EUR | 877286 | -5.63% | INVALID_5M | 100/5 | 99/0 |
| F-EUR | 871052 | -7.36% | INVALID_15M, INVALID_5M | 100/15 | 99/2 |
| MORPHO-EUR | 832387 | +8.17% | INVALID_15M, INVALID_5M | 100/8 | 99/1 |
| KAS-EUR | 800580 | +6.30% | INVALID_5M | 99/3 | 99/0 |
| C-EUR | 740677 | +4.63% | INVALID_5M | 99/1 | 99/0 |
| JUP-EUR | 732422 | +4.17% | INVALID_5M | 100/5 | 99/0 |
| STX-EUR | 639511 | +11.19% | INVALID_15M, INVALID_5M | 99/3 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
