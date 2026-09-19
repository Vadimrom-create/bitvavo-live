# Audit qualité des données Bitvavo

Scan : 2026-09-19T17:33:46.004652+00:00 (20260919T173219Z-a4fcdb6f)
Univers : 427 | strategy-grade : 35 | rejetés : 392
5m valides : 37 | 15m valides : 93 | deux intervalles valides : 35

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 390 |
| INVALID_15M | 334 |
| MISSING_LATEST_CLOSED_CANDLE | 224 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 390 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 334 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| STRK-EUR | 2173829 | +17.43% | INVALID_5M | 99/1 | 99/0 |
| APT-EUR | 1858966 | +6.50% | INVALID_5M | 99/2 | 99/0 |
| CAP-EUR | 1833577 | -15.90% | INVALID_15M | 99/0 | 99/1 |
| POL-EUR | 1523921 | +3.41% | INVALID_5M | 99/3 | 99/0 |
| LTC-EUR | 1516152 | +2.66% | INVALID_5M | 99/1 | 99/0 |
| WLD-EUR | 1417348 | +4.05% | INVALID_5M | 99/1 | 99/0 |
| HBAR-EUR | 1411305 | +4.20% | INVALID_5M | 99/1 | 99/0 |
| OP-EUR | 1220316 | +7.56% | INVALID_5M | 99/8 | 99/0 |
| VET-EUR | 1133015 | +10.53% | INVALID_5M | 99/1 | 99/0 |
| F-EUR | 1095230 | -15.51% | INVALID_5M | 99/5 | 99/0 |
| SKY-EUR | 1063151 | -0.28% | INVALID_15M, INVALID_5M | 100/6 | 100/1 |
| DOT-EUR | 953651 | +0.04% | INVALID_5M | 100/2 | 100/0 |
| BCH-EUR | 934839 | +2.21% | INVALID_5M | 100/4 | 100/0 |
| AAVE-EUR | 912513 | +2.80% | INVALID_5M | 99/5 | 99/0 |
| COTI-EUR | 898990 | -2.62% | INVALID_5M | 100/1 | 100/0 |
| MORPHO-EUR | 812098 | +9.98% | INVALID_5M | 100/3 | 100/0 |
| KAS-EUR | 807453 | +8.59% | INVALID_5M | 99/1 | 99/0 |
| HEI-EUR | 786915 | +13.35% | INVALID_5M | 99/3 | 99/0 |
| JUP-EUR | 738219 | +4.60% | INVALID_5M | 99/7 | 99/0 |
| RAY-EUR | 654143 | +2.84% | INVALID_5M | 99/2 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
