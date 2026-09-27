# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T20:34:21.948106+00:00
État : OK | marchés EUR : 427 | V4 : 384 | données valides : 427
Récupération : 2026-09-27T20:33:51.374661+00:00 | âge ticker : 150.9 s | durée : 154.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ARB-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- CC-EUR : 0.12031 € ; score 93.35/100 ; SURVEILLE ; seuil achat non atteint
- AXS-EUR : 1.0264 € ; score 91.69/100 ; SURVEILLE ; seuil achat non atteint
- ETHFI-EUR : 0.63472 € ; score 89.12/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- CTR-EUR : 0.01066 € ; score 88.59/100 ; SURVEILLE ; LOW_LIQUIDITY, VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- GMT-EUR : 0.007843 € ; score 88.06/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 165.467 | +56.16 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.2809 | +43.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.94185 | +30.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INX-EUR | 0.006604 | +29.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| W-EUR | 0.0139 | +23.90 % | DETECTED_EARLY | NONE | NONE |
| GLMR-EUR | 0.007379 | +18.52 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GRT-EUR | 0.02844 | +17.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRC-EUR | 0.0011606 | +15.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.23021 | +14.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AUDIO-EUR | 0.015858 | +14.28 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1644 scans ; 703356 observations ; 1170 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
