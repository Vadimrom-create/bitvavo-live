# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T23:42:03.835266+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-24T23:41:30.587957+00:00 | âge ticker : 150.3 s | durée : 151.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- XVG-EUR : 0.002662 € ; score 83.96/100 ; SURVEILLE ; seuil achat non atteint
- SYN-EUR : 0.176173 € ; score 83.52/100 ; SURVEILLE ; seuil achat non atteint
- SENT-EUR : 0.019086 € ; score 82.84/100 ; SURVEILLE ; WICK_SETUP
- MOG-EUR : 1.1371e-07 € ; score 82.06/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ICP-EUR : 2.7385 € ; score 81.61/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.063007 | +47.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.0229 | +29.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XAI-EUR | 0.008921 | +28.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 79.002 | +27.30 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.60883 | +26.84 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.038581 | +26.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ONDO-EUR | 0.45771 | +26.44 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.098577 | +24.59 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.17108 | +23.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DYM-EUR | 0.018764 | +19.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1400 scans ; 599168 observations ; 780 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
