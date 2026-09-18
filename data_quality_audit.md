# Audit qualité des données Bitvavo

Scan : 2026-09-18T23:36:32.897419+00:00 (20260918T233430Z-818d7d84)
Univers : 427 | strategy-grade : 26 | rejetés : 401
5m valides : 27 | 15m valides : 74 | deux intervalles valides : 26

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 400 |
| INVALID_15M | 353 |
| MISSING_LATEST_CLOSED_CANDLE | 298 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 400 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 353 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| UNI-EUR | 6300160 | +15.49% | INVALID_5M | 99/3 | 99/0 |
| PUMP-EUR | 2787981 | +4.31% | INVALID_5M | 99/4 | 99/0 |
| USDC-EUR | 2750448 | -0.17% | INVALID_5M | 100/1 | 99/0 |
| LSK-EUR | 2714601 | -1.23% | INVALID_5M | 99/1 | 99/0 |
| FET-EUR | 2694366 | +7.33% | INVALID_5M | 100/1 | 99/0 |
| WLD-EUR | 2558720 | +11.09% | INVALID_5M | 100/1 | 99/0 |
| XLM-EUR | 1960896 | +4.67% | INVALID_5M | 100/1 | 99/0 |
| INJ-EUR | 1854579 | +14.85% | INVALID_5M | 99/5 | 99/0 |
| COTI-EUR | 1737762 | -16.94% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/3 | 100/0 |
| RAY-EUR | 1549009 | +20.63% | INVALID_5M | 99/2 | 99/0 |
| LTC-EUR | 1478052 | +6.90% | INVALID_5M | 100/2 | 99/0 |
| APT-EUR | 1288704 | +21.49% | INVALID_5M | 100/1 | 99/0 |
| DOT-EUR | 1281536 | +4.24% | INVALID_5M | 100/3 | 99/0 |
| POL-EUR | 1259113 | +8.77% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/1 | 100/0 |
| HBAR-EUR | 1182534 | +6.07% | INVALID_5M | 99/1 | 99/0 |
| SKY-EUR | 1083049 | +17.18% | INVALID_15M, INVALID_5M | 100/13 | 99/1 |
| DRIFT-EUR | 1073823 | +1.35% | INVALID_5M | 99/1 | 99/0 |
| XPL-EUR | 988002 | +7.43% | INVALID_5M | 99/7 | 99/0 |
| AAVE-EUR | 945758 | +8.07% | INVALID_5M | 100/3 | 99/0 |
| LPT-EUR | 885786 | +16.33% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 99/2 | 100/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
