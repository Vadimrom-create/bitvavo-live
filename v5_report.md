# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T10:36:18.915658+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T10:35:47.170461+00:00 | âge ticker : 156.8 s | durée : 158.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- INIT-EUR : 0.085977 € ; score 90.43/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- ATH-EUR : 0.005218 € ; score 88.16/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- POPCAT-EUR : 0.050479 € ; score 87.37/100 ; SURVEILLE ; seuil achat non atteint
- SENT-EUR : 0.019318 € ; score 87.18/100 ; SURVEILLE ; WICK_SETUP
- ZEN-EUR : 6.6446 € ; score 86.31/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 87.43 | +40.24 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.675 | +33.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.48462 | +31.68 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.101047 | +31.53 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.19498 | +29.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.053398 | +26.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FET-EUR | 0.21124 | +23.17 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.038174 | +20.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHIP-EUR | 0.043839 | +19.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| JTO-EUR | 0.47485 | +19.90 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1437 scans ; 614967 observations ; 829 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
