# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T09:51:19.327640+00:00
État : OK | marchés EUR : 427 | V4 : 382 | données valides : 427
Récupération : 2026-09-27T09:50:46.471837+00:00 | âge ticker : 149.4 s | durée : 150.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AXS-EUR : INSUFFICIENT_NET_RISK_REWARD
- CC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- GRAM-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ARKM-EUR : 0.12399 € ; score 93.40/100 ; SURVEILLE ; seuil achat non atteint
- DATAIP-EUR : 0.2039 € ; score 93.02/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : 0.105985 € ; score 89.52/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : 0.24866 € ; score 87.23/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- CELR-EUR : 0.002714 € ; score 86.63/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 154.732 | +66.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008735 | +49.32 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.27089 | +45.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.99896 | +39.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AMP-EUR | 0.0006003 | +30.84 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| HFT-EUR | 0.007006 | +26.12 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| W-EUR | 0.013655 | +24.08 % | DETECTED_EARLY | NONE | NONE |
| AGI-EUR | 0.00619 | +21.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XVG-EUR | 0.0032383 | +18.22 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| WLD-EUR | 0.49064 | +17.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1606 scans ; 687130 observations ; 1112 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
