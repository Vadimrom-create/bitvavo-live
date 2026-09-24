# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T23:26:11.873332+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-24T23:25:39.961946+00:00 | âge ticker : 156.4 s | durée : 157.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

## SURVEILLE

- DRIFT-EUR : 0.01651 € ; score 85.49/100 ; SURVEILLE ; SPREAD_RISK
- ICP-EUR : 2.7474 € ; score 83.24/100 ; SURVEILLE ; WICK_SETUP
- DATAIP-EUR : 0.2005 € ; score 81.42/100 ; SURVEILLE ; seuil achat non atteint
- SOMI-EUR : 0.17354 € ; score 81.01/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- PYTH-EUR : 0.059458 € ; score 80.85/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.063145 | +50.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.023199 | +29.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 78.973 | +27.41 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.60812 | +26.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XAI-EUR | 0.0087224 | +26.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.45679 | +25.88 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.038448 | +25.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XPL-EUR | 0.097783 | +23.84 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.17146 | +23.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DYM-EUR | 0.018779 | +19.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1399 scans ; 598741 observations ; 775 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
