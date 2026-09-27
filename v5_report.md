# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T04:52:03.775108+00:00
État : OK | marchés EUR : 427 | V4 : 382 | données valides : 427
Récupération : 2026-09-27T04:51:34.409168+00:00 | âge ticker : 150.6 s | durée : 151.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WOO-EUR : 0.011734 € ; score 91.74/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ADA-EUR : 0.21993 € ; score 91.21/100 ; SURVEILLE ; seuil achat non atteint
- ENJ-EUR : 0.026384 € ; score 91.20/100 ; SURVEILLE ; seuil achat non atteint
- POWR-EUR : 0.061135 € ; score 90.77/100 ; SURVEILLE ; LOW_LIQUIDITY, STABILITY_HOLD
- LUMIA-EUR : 0.081163 € ; score 89.76/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 164.82 | +89.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.2545 | +39.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006125 | +36.69 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.01669 | +25.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.007217 | +24.11 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.001295 | +23.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RUNE-EUR | 0.70219 | +20.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.85659 | +19.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.006151 | +18.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TAIKO-EUR | 0.09611 | +18.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1589 scans ; 679871 observations ; 1080 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
