# Audit qualité des données Bitvavo

Scan : 2026-09-28T13:53:50.027907+00:00 (20260928T135213Z-ae322637)
Univers : 428 | strategy-grade : 427 | rejetés : 1
5m valides : 427 | 15m valides : 427 | deux intervalles valides : 427

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
| XDP-EUR | 965684 | +24.27% | INVALID_15M, INVALID_5M | 9/0 | 3/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
