# Audit qualité des données Bitvavo

Scan : 2026-09-29T12:54:06.462417+00:00 (20260929T125231Z-689290b2)
Univers : 429 | strategy-grade : 428 | rejetés : 1
5m valides : 428 | 15m valides : 428 | deux intervalles valides : 428

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
| DRV-EUR | 397481 | +3.70% | INVALID_15M, INVALID_5M | 23/0 | 8/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
