# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T13:45:16.519035+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 427
Récupération : 2026-09-25T13:44:18.291622+00:00 | âge ticker : 183.9 s | durée : 185.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.
- OP-EUR : 0.12252 € | IGNITION | score 87.22/100 | entrée 7.45/10
  Entrée 0.12268 € ; stop 0.1179 € ; TP1 0.13223 € ; TP2 0.13701 € ; montant 250.00 € ; risque théorique 11.46 € ; R/R net 1.54.
  Chase risk : 2.702/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- BABY-EUR : 0.011478 € ; score 89.03/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SAPIEN-EUR : 0.069699 € ; score 86.85/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- AEVO-EUR : 0.022652 € ; score 85.37/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RARE-EUR : 0.012071 € ; score 84.87/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- AXS-EUR : 1.0141 € ; score 84.78/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.063011 | +41.32 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| TREAD-EUR | 0.68066 | +35.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.19869 | +29.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XPL-EUR | 0.098501 | +24.97 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NIL-EUR | 0.116378 | +23.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 83.117 | +23.26 % | DETECTED_EARLY | NONE | NONE |
| DBR-EUR | 0.020795 | +18.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.08534 | +18.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PIXEL-EUR | 0.0055266 | +17.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FET-EUR | 0.21179 | +17.17 % | DETECTED_EARLY | NONE | NONE |

Historique : 1447 scans ; 619237 observations ; 856 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
