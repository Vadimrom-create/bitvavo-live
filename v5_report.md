# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T17:24:06.010438+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-25T17:23:33.679977+00:00 | âge ticker : 150.6 s | durée : 151.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- GRT-EUR : 0.023812 € ; score 91.87/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- CELR-EUR : 0.0027357 € ; score 90.91/100 ; SURVEILLE ; WICK_SETUP
- ATH-EUR : 0.0053318 € ; score 90.79/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BABY-EUR : 0.01172 € ; score 88.32/100 ; SURVEILLE ; seuil achat non atteint
- EDEN-EUR : 0.055372 € ; score 86.64/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.067992 | +56.04 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.20448 | +27.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WMTX-EUR | 0.021876 | +26.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RARE-EUR | 0.014283 | +23.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.46625 | +21.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.73533 | +19.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.23057 | +19.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.08629 | +18.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.67154 | +16.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SPK-EUR | 0.021786 | +15.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1459 scans ; 624361 observations ; 877 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
