# Audit qualité des données Bitvavo

Scan : 2026-09-30T11:42:07.255875+00:00 (20260930T114040Z-087c24b1)
Univers : 430 | strategy-grade : 429 | rejetés : 1
5m valides : 429 | 15m valides : 429 | deux intervalles valides : 429

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_15M | 1 |
| INVALID_5M | 1 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|
| INSUFFICIENT_CLOSED_CANDLES | 1 |

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| INSUFFICIENT_CLOSED_CANDLES | 1 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| CT-EUR | 958948 | +65.12% | INVALID_15M, INVALID_5M | 20/0 | 6/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
