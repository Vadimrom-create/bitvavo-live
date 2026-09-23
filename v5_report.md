# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T05:18:17.294450+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-23T05:17:48.628207+00:00 | âge ticker : 147.7 s | durée : 149.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- F-EUR : 0.0033457 € ; score 90.27/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- LIGHTER-EUR : 4.5191 € ; score 90.10/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- ZK-EUR : 0.010731 € ; score 89.77/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- RECALL-EUR : 0.041998 € ; score 89.47/100 ; SURVEILLE ; seuil achat non atteint
- FUN-EUR : 0.017539 € ; score 87.63/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.089961 | +43.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.31576 | +33.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.310235 | +32.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 297.26 | +29.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.48905 | +28.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CHR-EUR | 0.01955 | +27.43 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SUPER-EUR | 0.16408 | +24.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PENGU-EUR | 0.0093412 | +22.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2343 | +22.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FLOCK-EUR | 0.075784 | +20.09 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1245 scans ; 533107 observations ; 595 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
