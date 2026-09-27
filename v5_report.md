# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T07:20:34.323665+00:00
État : OK | marchés EUR : 427 | V4 : 381 | données valides : 427
Récupération : 2026-09-27T07:20:05.920483+00:00 | âge ticker : 144.8 s | durée : 145.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- GRAM-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- AXS-EUR : 1.0383 € ; score 93.24/100 ; SURVEILLE ; WICK_SETUP
- ZK-EUR : 0.011613 € ; score 93.13/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- WOO-EUR : 0.011975 € ; score 91.74/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- UMA-EUR : 0.37362 € ; score 90.27/100 ; SURVEILLE ; STABILITY_HOLD
- ZORA-EUR : 0.007727 € ; score 89.89/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 148.4 | +67.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.26218 | +38.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008055 | +36.53 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AMP-EUR | 0.0006059 | +34.26 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006453 | +26.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.120962 | +20.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.01319 | +20.67 % | DETECTED_EARLY | NONE | NONE |
| HFT-EUR | 0.006589 | +20.26 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| RUNE-EUR | 0.7 | +17.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PYTH-EUR | 0.075729 | +15.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1597 scans ; 683287 observations ; 1095 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
