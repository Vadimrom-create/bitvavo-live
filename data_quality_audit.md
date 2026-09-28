# Audit qualité des données Bitvavo

Scan : 2026-09-28T17:43:18.983697+00:00 (20260928T174146Z-4d2908f5)
Univers : 428 | strategy-grade : 427 | rejetés : 1
5m valides : 428 | 15m valides : 427 | deux intervalles valides : 427

## Causes de rejet globales

| Cause | Marchés |
|---|---:|
| INVALID_15M | 1 |

## Causes intrinsèques 5m

| Cause | Marchés |
|---|---:|

## Causes intrinsèques 15m

| Cause | Marchés |
|---|---:|
| INSUFFICIENT_CLOSED_CANDLES | 1 |

## Marchés rejetés les plus liquides

| Marché | Vol. 24h € | 24h | Causes | 5m bars/gaps manquants | 15m bars/gaps manquants |
|---|---:|---:|---|---:|---:|
| XDP-EUR | 2467135 | -30.96% | INVALID_15M | 55/0 | 18/0 |

Lecture : bars/gaps manquants = nombre de bougies closes reçues / nombre d’intervalles sans bougie à l’intérieur des 25 dernières bougies observées.
Ce fichier est purement diagnostique : aucune règle de trading n’est modifiée.
