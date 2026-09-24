# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T20:57:57.958185+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-24T20:57:23.947672+00:00 | âge ticker : 149.8 s | durée : 150.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- AXL-EUR : 0.045352 € ; score 88.37/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- AERO-EUR : 0.61583 € ; score 87.95/100 ; SURVEILLE ; seuil achat non atteint
- SNX-EUR : 0.22347 € ; score 86.46/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- TRUMP-EUR : 1.8486 € ; score 84.70/100 ; SURVEILLE ; seuil achat non atteint
- BEAM-EUR : 0.001776 € ; score 84.42/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| LSK-EUR | 0.40275 | +39.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XAI-EUR | 0.0094352 | +37.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.57275 | +25.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.44844 | +24.37 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 76.644 | +23.38 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.094501 | +21.21 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.037068 | +20.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.16769 | +20.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0161957 | +18.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.100644 | +18.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1389 scans ; 594471 observations ; 762 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
