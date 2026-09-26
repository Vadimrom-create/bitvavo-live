# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T20:18:50.375262+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T20:18:15.614238+00:00 | âge ticker : 149.1 s | durée : 149.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- EIGEN-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- SHIB-EUR : 5.1866e-06 € ; score 87.72/100 ; SURVEILLE ; seuil achat non atteint
- HNT-EUR : 0.4862 € ; score 86.43/100 ; SURVEILLE ; SPREAD_RISK
- AEVO-EUR : 0.024287 € ; score 84.71/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- FOLD-EUR : 0.055185 € ; score 83.53/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- CC-EUR : 0.11858 € ; score 83.22/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017347 | +109.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0007528 | +69.70 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.0194 | +35.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.118338 | +32.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 104.528 | +21.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.043959 | +20.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.0615 | +19.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KAS-EUR | 0.042952 | +17.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LAPTOP-EUR | 0.07475 | +15.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.00592 | +15.20 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1559 scans ; 667061 observations ; 1048 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
