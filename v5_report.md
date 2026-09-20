# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T21:56:05.723851+00:00
État : OK | marchés EUR : 426 | V4 : 380 | données valides : 426
Récupération : 2026-09-20T21:55:31.153893+00:00 | âge ticker : 155.7 s | durée : 156.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- ZRO-EUR : 1.049 € ; score 93.18/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- IOST-EUR : 0.0007597 € ; score 91.40/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- STX-EUR : 0.28576 € ; score 84.48/100 ; SURVEILLE ; seuil achat non atteint
- PENDLE-EUR : 2.3392 € ; score 83.65/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.37192 € ; score 82.45/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.032748 | +50.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.24623 | +33.44 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0008128 | +33.38 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.0564 | +29.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.034669 | +20.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6438 | +18.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EPIC-EUR | 0.49102 | +17.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LUNA2-EUR | 0.048658 | +17.36 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| KMNO-EUR | 0.027803 | +16.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 9.8804 | +16.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1020 scans ; 437257 observations ; 274 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
