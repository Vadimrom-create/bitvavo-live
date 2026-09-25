# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T23:54:41.767873+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-24T23:54:08.298193+00:00 | âge ticker : 157.1 s | durée : 158.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- NEO-EUR : 2.2914 € ; score 84.13/100 ; SURVEILLE ; seuil achat non atteint
- XLM-EUR : 0.19007 € ; score 83.27/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TNSR-EUR : 0.033715 € ; score 81.00/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- MANTRA-EUR : 0.004132 € ; score 80.60/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- GMT-EUR : 0.007566 € ; score 79.27/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.063128 | +50.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 79.047 | +27.24 % | DETECTED_EARLY | NONE | NONE |
| ONDO-EUR | 0.46208 | +27.24 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.60883 | +25.97 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.038301 | +25.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XAI-EUR | 0.0086576 | +24.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XPL-EUR | 0.098509 | +24.33 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| DBR-EUR | 0.022103 | +24.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.17108 | +23.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DYM-EUR | 0.018693 | +19.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1401 scans ; 599595 observations ; 782 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
