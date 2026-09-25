# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T05:18:50.749710+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T05:18:18.523842+00:00 | âge ticker : 148.6 s | durée : 149.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ALLO-EUR : 0.250901 € ; score 88.84/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- VIRTUAL-EUR : 0.67024 € ; score 88.55/100 ; SURVEILLE ; seuil achat non atteint
- BIGTIME-EUR : 0.007604 € ; score 87.41/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.6196 € ; score 87.15/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LRC-EUR : 0.008449 € ; score 84.66/100 ; SURVEILLE ; LOW_LIQUIDITY

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.68719 | +38.51 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 83.037 | +30.88 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.099915 | +26.18 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.47123 | +25.34 % | DETECTED_EARLY | NONE | NONE |
| EDGE-EUR | 0.089601 | +24.35 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.0383 | +21.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.17646 | +16.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XAI-EUR | 0.0081981 | +16.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.021765 | +15.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TAI-EUR | 0.00406 | +14.53 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1419 scans ; 607281 observations ; 810 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
