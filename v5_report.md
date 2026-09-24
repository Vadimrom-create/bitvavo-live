# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T04:34:04.585681+00:00
État : OK | marchés EUR : 426 | V4 : 404 | données valides : 426
Récupération : 2026-09-24T04:33:31.108771+00:00 | âge ticker : 147.0 s | durée : 147.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- GMT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PYTH-EUR : 0.056787 € ; score 91.71/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0079048 € ; score 91.67/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : 62.567 € ; score 91.17/100 ; SURVEILLE ; seuil achat non atteint
- OP-EUR : 0.10987 € ; score 90.94/100 ; SURVEILLE ; seuil achat non atteint
- KAS-EUR : 0.034162 € ; score 89.40/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.11674 | +36.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0020872 | +34.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CVC-EUR | 0.0293 | +16.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.31619 | +15.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.018728 | +13.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.040445 | +13.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMU-EUR | 0.0019065 | +12.81 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOSO-EUR | 0.28709 | +9.25 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| CPOOL-EUR | 0.028949 | +8.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.3402 | +7.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1328 scans ; 568465 observations ; 681 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
