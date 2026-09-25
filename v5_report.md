# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T04:22:36.307123+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T04:22:02.249356+00:00 | âge ticker : 150.4 s | durée : 151.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : EXTENDED_24H, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- CAKE-EUR : 2.4153 € ; score 84.62/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- LTC-EUR : 62.24 € ; score 79.71/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- PYTH-EUR : 0.060209 € ; score 78.49/100 ; SURVEILLE ; seuil achat non atteint
- INJ-EUR : 7.0195 € ; score 77.98/100 ; SURVEILLE ; seuil achat non atteint
- ICNT-EUR : 0.08985 € ; score 77.77/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 83.896 | +34.24 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.102683 | +30.36 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 0.63495 | +29.62 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| EDGE-EUR | 0.092592 | +28.50 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.47117 | +26.78 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.039319 | +25.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.17197 | +16.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.19952 | +15.73 % | DETECTED_EARLY | NONE | NONE |
| XAI-EUR | 0.0081432 | +15.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.021488 | +14.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1416 scans ; 606000 observations ; 804 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
