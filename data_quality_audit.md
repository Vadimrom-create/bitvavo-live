# Audit qualité des données Bitvavo

Scan : 2026-09-20T14:29:02.022092+00:00 (20260920T142735Z-058f7319)
Univers : 426 | strategy-grade : 33 | rejetés : 393
5m valides : 34 | 15m valides : 77 | deux intervalles valides : 33

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 392 |
| INVALID_15M | 349 |
| MISSING_LATEST_CLOSED_CANDLE | 289 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 392 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 349 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| FET-EUR | 2142866 | -7.37% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 1809221 | -5.33% | INVALID_5M | 99/1 | 99/0 |
| PUMP-EUR | 1434534 | -2.69% | INVALID_5M | 99/4 | 99/0 |
| WLD-EUR | 1419174 | -2.72% | INVALID_5M | 99/3 | 99/0 |
| UNI-EUR | 1419006 | -4.52% | INVALID_5M | 99/2 | 99/0 |
| CAKE-EUR | 1326043 | +2.35% | INVALID_5M | 100/1 | 99/0 |
| LSK-EUR | 1172072 | -13.33% | INVALID_5M | 99/1 | 99/0 |
| LTC-EUR | 1065285 | -1.72% | INVALID_5M | 99/2 | 99/0 |
| ARB-EUR | 1065097 | -2.78% | INVALID_5M | 99/1 | 99/0 |
| FIL-EUR | 904684 | -7.52% | INVALID_15M, INVALID_5M | 92/14 | 99/4 |
| STX-EUR | 898295 | -0.08% | INVALID_15M, INVALID_5M | 99/15 | 99/2 |
| DOT-EUR | 835058 | -3.01% | INVALID_5M | 99/4 | 99/0 |
| SHIB-EUR | 771163 | -3.34% | INVALID_5M | 100/3 | 99/0 |
| SKL-EUR | 748162 | +5.57% | INVALID_5M | 99/2 | 99/0 |
| BCH-EUR | 742388 | -3.42% | INVALID_15M, INVALID_5M | 91/13 | 99/2 |
| APT-EUR | 741121 | -3.43% | INVALID_5M | 99/5 | 99/0 |
| USELESS-EUR | 732883 | -6.24% | INVALID_5M | 99/3 | 99/0 |
| ZIL-EUR | 700717 | +4.45% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/4 | 100/0 |
| S-EUR | 671002 | +9.42% | INVALID_5M | 99/1 | 99/0 |
| DRIFT-EUR | 635261 | +6.05% | INVALID_15M, INVALID_5M | 99/2 | 99/1 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
