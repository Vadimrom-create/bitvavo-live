# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T22:22:21.757926+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-24T22:21:50.045692+00:00 | âge ticker : 185.8 s | durée : 186.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- IO-EUR : 0.1389 € ; score 90.62/100 ; SURVEILLE ; seuil achat non atteint
- DOGE-EUR : 0.083568 € ; score 89.25/100 ; SURVEILLE ; seuil achat non atteint
- XLM-EUR : 0.18775 € ; score 84.84/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : 0.095124 € ; score 84.39/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : 0.10117 € ; score 83.46/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PEAQ-EUR | 0.041287 | +33.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.057893 | +32.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XAI-EUR | 0.0090955 | +31.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.59643 | +30.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 79.316 | +27.70 % | DETECTED_EARLY | NONE | NONE |
| LSK-EUR | 0.38208 | +26.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.45447 | +24.60 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.098827 | +23.85 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.16912 | +22.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DYM-EUR | 0.018224 | +16.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1395 scans ; 597033 observations ; 766 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
