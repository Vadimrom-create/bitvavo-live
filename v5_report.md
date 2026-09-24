# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T23:08:36.942773+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-24T23:08:03.344975+00:00 | âge ticker : 150.3 s | durée : 151.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LTC-EUR : EXTENDED_24H, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- DATAIP-EUR : 0.2006 € ; score 90.34/100 ; SURVEILLE ; WICK_SETUP
- GMT-EUR : 0.007592 € ; score 83.05/100 ; SURVEILLE ; WICK_SETUP
- PYTH-EUR : 0.059993 € ; score 82.12/100 ; SURVEILLE ; seuil achat non atteint
- ICP-EUR : 2.7249 € ; score 80.07/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- YGG-EUR : 0.023791 € ; score 79.80/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.059559 | +42.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.023356 | +30.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.60316 | +28.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XAI-EUR | 0.0088217 | +27.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 78.614 | +26.49 % | DETECTED_EARLY | NONE | NONE |
| ONDO-EUR | 0.45475 | +25.33 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.038326 | +24.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XPL-EUR | 0.098441 | +24.16 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.17074 | +22.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LSK-EUR | 0.36452 | +21.05 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1398 scans ; 598314 observations ; 774 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
