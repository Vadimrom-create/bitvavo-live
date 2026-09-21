# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T08:26:12.636796+00:00
État : OK | marchés EUR : 426 | V4 : 378 | données valides : 426
Récupération : 2026-09-21T08:25:44.047816+00:00 | âge ticker : 151.5 s | durée : 152.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PENDLE-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MERL-EUR : 0.023609 € ; score 92.71/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- SOL-EUR : 98.651 € ; score 91.35/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ZEN-EUR : 6.8907 € ; score 91.20/100 ; SURVEILLE ; seuil achat non atteint
- CHILLGUY-EUR : 0.0119821 € ; score 89.52/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MEGA-EUR : 0.03835 € ; score 89.35/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.057033 | +71.76 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.0009665 | +59.02 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.25108 | +37.20 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.058957 | +36.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.032889 | +34.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.029962 | +27.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.51292 | +24.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| VVV-EUR | 29.9232 | +24.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NEAR-EUR | 3.7925 | +23.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.0372 | +20.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1060 scans ; 454297 observations ; 330 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
