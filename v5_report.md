# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T11:02:10.732562+00:00
État : OK | marchés EUR : 430 | V4 : 390 | données valides : 429
Récupération : 2026-09-30T11:01:38.175594+00:00 | âge ticker : 157.8 s | durée : 159.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/430 ; 15 min 429/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NEAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VIRTUAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SPK-EUR : 0.021716 € ; score 91.16/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- WIF-EUR : 0.22398 € ; score 91.01/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BEAM-EUR : 0.0017683 € ; score 88.42/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, WICK_SETUP
- IO-EUR : 0.14449 € ; score 87.72/100 ; SURVEILLE ; seuil achat non atteint
- RSR-EUR : 0.0015139 € ; score 86.62/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.5662 | +75.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.38839 | +62.51 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SOON-EUR | 0.39807 | +32.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.100361 | +29.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.27767 | +28.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008549 | +27.07 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.069388 | +22.83 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TRAC-EUR | 0.39449 | +19.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 260.34 | +15.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.88843 | +14.60 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1835 scans ; 785128 observations ; 1368 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
