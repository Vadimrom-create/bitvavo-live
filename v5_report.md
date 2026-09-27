# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T09:36:21.988184+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T09:35:51.020344+00:00 | âge ticker : 145.4 s | durée : 146.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- FLUX-EUR : 0.065071 € ; score 92.38/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- 0G-EUR : 0.22902 € ; score 92.00/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SUSHI-EUR : 0.2394 € ; score 90.95/100 ; SURVEILLE ; seuil achat non atteint
- ENS-EUR : 6.23 € ; score 90.59/100 ; SURVEILLE ; LOW_LIQUIDITY
- GLM-EUR : 0.11587 € ; score 88.82/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 154.96 | +68.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.009 | +55.71 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.26688 | +42.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0005997 | +31.00 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| HFT-EUR | 0.007094 | +29.29 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| TREAD-EUR | 0.9186 | +28.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.006322 | +24.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| W-EUR | 0.013556 | +23.37 % | DETECTED_EARLY | NONE | NONE |
| TRIA-EUR | 0.004231 | +17.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XVG-EUR | 0.003189 | +17.08 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |

Historique : 1605 scans ; 686703 observations ; 1107 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
