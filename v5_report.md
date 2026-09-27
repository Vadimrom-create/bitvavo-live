# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T10:41:53.327405+00:00
État : OK | marchés EUR : 427 | V4 : 382 | données valides : 427
Récupération : 2026-09-27T10:40:55.728894+00:00 | âge ticker : 175.6 s | durée : 177.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- BRETT-EUR : 0.005612 € ; score 93.18/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- GMT-EUR : 0.007968 € ; score 92.43/100 ; SURVEILLE ; seuil achat non atteint
- DYM-EUR : 0.017993 € ; score 91.35/100 ; SURVEILLE ; SPREAD_RISK
- APE-EUR : 0.1403 € ; score 90.90/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- KAIA-EUR : 0.031909 € ; score 89.66/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 151.696 | +59.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008967 | +53.05 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 1.01641 | +42.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AMP-EUR | 0.0006349 | +38.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.25745 | +36.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.124898 | +28.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HFT-EUR | 0.006903 | +24.27 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AGI-EUR | 0.006393 | +23.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.54531 | +18.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.013251 | +17.66 % | DETECTED_EARLY | NONE | NONE |

Historique : 1609 scans ; 688411 observations ; 1118 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
