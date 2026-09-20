# Audit qualité des données Bitvavo

Scan : 2026-09-20T17:26:23.784997+00:00 (20260920T172459Z-b8e10320)
Univers : 426 | strategy-grade : 40 | rejetés : 386
5m valides : 45 | 15m valides : 82 | deux intervalles valides : 40

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 381 |
| INVALID_15M | 344 |
| MISSING_LATEST_CLOSED_CANDLE | 254 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 381 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 344 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| WLD-EUR | 1739273 | +0.94% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1348811 | +3.36% | INVALID_5M | 99/7 | 99/0 |
| LSK-EUR | 1244766 | -5.76% | INVALID_5M | 99/1 | 99/0 |
| DOT-EUR | 961692 | +1.77% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 956775 | +6.65% | INVALID_5M | 99/1 | 99/0 |
| STX-EUR | 899942 | +4.69% | INVALID_15M, INVALID_5M | 99/9 | 99/3 |
| FIL-EUR | 853568 | -12.00% | INVALID_15M, INVALID_5M | 99/6 | 99/4 |
| SKL-EUR | 807978 | +6.81% | INVALID_5M | 100/3 | 99/0 |
| SHIB-EUR | 758176 | -1.84% | INVALID_5M | 99/3 | 99/0 |
| S-EUR | 752639 | +13.67% | INVALID_5M | 99/2 | 99/0 |
| APT-EUR | 741840 | +1.11% | INVALID_5M | 100/4 | 99/0 |
| ZIL-EUR | 712392 | +6.33% | INVALID_15M, INVALID_5M | 100/20 | 99/2 |
| AAVE-EUR | 661873 | -4.66% | INVALID_5M | 99/1 | 99/0 |
| XPL-EUR | 655931 | -1.92% | INVALID_5M | 99/1 | 99/0 |
| POL-EUR | 621684 | +2.50% | INVALID_5M | 100/3 | 99/0 |
| KMNO-EUR | 603045 | +15.59% | INVALID_15M, INVALID_5M | 88/6 | 99/2 |
| BCH-EUR | 596619 | -0.93% | INVALID_15M, INVALID_5M | 97/6 | 99/1 |
| TIA-EUR | 588722 | +0.05% | INVALID_15M, INVALID_5M | 100/7 | 99/1 |
| GRASS-EUR | 580519 | +3.80% | INVALID_5M | 100/2 | 99/0 |
| VVV-EUR | 562358 | +2.34% | INVALID_5M | 100/3 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
