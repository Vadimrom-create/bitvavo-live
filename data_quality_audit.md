# Audit qualité des données Bitvavo

Scan : 2026-09-20T10:52:40.681294+00:00 (20260920T105107Z-26200ae4)
Univers : 426 | strategy-grade : 31 | rejetés : 395
5m valides : 32 | 15m valides : 73 | deux intervalles valides : 31

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_5M | 394 |
| INVALID_15M | 353 |
| MISSING_LATEST_CLOSED_CANDLE | 288 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 394 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| CANDLE_GAPS | 353 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| HYPE-EUR | 7131303 | -0.91% | INVALID_5M | 99/1 | 99/0 |
| XLM-EUR | 2529799 | -1.97% | INVALID_5M | 100/1 | 99/0 |
| CAP-EUR | 2062502 | -24.03% | INVALID_5M | 99/6 | 99/0 |
| UNI-EUR | 1589606 | -3.26% | INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 100/1 | 100/0 |
| DOGE-EUR | 1512712 | -3.46% | INVALID_5M | 100/1 | 99/0 |
| WLD-EUR | 1433836 | -1.18% | INVALID_5M | 100/1 | 99/0 |
| PUMP-EUR | 1416450 | -3.03% | INVALID_5M | 100/1 | 99/0 |
| LTC-EUR | 1361673 | -0.59% | INVALID_5M | 99/1 | 99/0 |
| LSK-EUR | 1236412 | -15.72% | INVALID_5M | 99/1 | 99/0 |
| CAKE-EUR | 1150238 | +0.82% | INVALID_15M, INVALID_5M | 99/1 | 99/3 |
| ARB-EUR | 1146710 | -0.27% | INVALID_5M | 99/1 | 99/0 |
| STRK-EUR | 1067210 | +1.61% | INVALID_5M | 99/1 | 99/0 |
| EPIC-EUR | 1016765 | +4.17% | INVALID_5M | 99/2 | 99/0 |
| STX-EUR | 1012677 | +6.00% | INVALID_5M | 100/2 | 99/0 |
| FIL-EUR | 852905 | -3.40% | INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE | 96/12 | 99/2 |
| APT-EUR | 852132 | -2.56% | INVALID_5M | 99/7 | 99/0 |
| USELESS-EUR | 836882 | -2.13% | INVALID_5M | 100/3 | 99/0 |
| BCH-EUR | 750694 | -1.83% | INVALID_15M, INVALID_5M | 82/17 | 99/1 |
| SHIB-EUR | 738384 | -2.01% | INVALID_5M | 100/1 | 99/0 |
| KAS-EUR | 715755 | +1.50% | INVALID_5M | 99/1 | 99/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
