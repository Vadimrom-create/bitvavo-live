# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T04:50:09.436400+00:00
État : OK | marchés EUR : 426 | V4 : 403 | données valides : 426
Récupération : 2026-09-24T04:49:40.103936+00:00 | âge ticker : 143.4 s | durée : 144.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- GMT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- 0G-EUR : 0.22324 € ; score 92.75/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- NEO-EUR : 2.2375 € ; score 90.85/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0079177 € ; score 90.26/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- G-EUR : 0.0050957 € ; score 89.87/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- BAT-EUR : 0.07833 € ; score 88.66/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.11985 | +42.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0020444 | +32.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.32177 | +18.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IMU-EUR | 0.0019887 | +17.67 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| DBR-EUR | 0.018693 | +13.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CVC-EUR | 0.02781 | +10.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.75734 | +10.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOSO-EUR | 0.28641 | +8.99 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| ZRO-EUR | 1.3475 | +8.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.029142 | +8.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1329 scans ; 568891 observations ; 681 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
