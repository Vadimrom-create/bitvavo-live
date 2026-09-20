# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T21:43:19.090247+00:00
État : OK | marchés EUR : 426 | V4 : 381 | données valides : 426
Récupération : 2026-09-20T21:42:44.585730+00:00 | âge ticker : 161.2 s | durée : 162.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- CAKE-EUR : 2.2301 € ; score 91.21/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FLUX-EUR : 0.050751 € ; score 87.02/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK
- STX-EUR : 0.28576 € ; score 85.24/100 ; SURVEILLE ; seuil achat non atteint
- ZRO-EUR : 1.0373 € ; score 84.10/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PENDLE-EUR : 2.3113 € ; score 82.08/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.033421 | +53.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0008154 | +34.02 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.24048 | +30.33 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.055433 | +27.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.49827 | +21.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| S-EUR | 0.034347 | +19.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6255 | +17.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVAX-EUR | 9.7724 | +17.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.027906 | +17.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELR-EUR | 0.003002 | +16.88 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1019 scans ; 436831 observations ; 274 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
