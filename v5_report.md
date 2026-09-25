# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T17:57:27.241715+00:00
État : OK | marchés EUR : 427 | V4 : 384 | données valides : 427
Récupération : 2026-09-25T17:56:27.293763+00:00 | âge ticker : 176.7 s | durée : 177.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AXS-EUR : INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- CAKE-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- XAI-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- XAI-EUR : 0.0080783 € ; score 92.24/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ALICE-EUR : 0.13715 € ; score 90.95/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- MOODENG-EUR : 0.043097 € ; score 89.44/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RSR-EUR : 0.0015476 € ; score 88.40/100 ; SURVEILLE ; seuil achat non atteint
- ATH-EUR : 0.0053404 € ; score 87.52/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.07117 | +65.13 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| WMTX-EUR | 0.024037 | +52.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.20417 | +29.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.4735 | +24.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.66097 | +24.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RARE-EUR | 0.014363 | +23.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.087874 | +20.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.74266 | +20.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.22717 | +19.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SPK-EUR | 0.021646 | +15.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1461 scans ; 625215 observations ; 878 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
