# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T07:21:59.818535+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-24T07:21:27.992678+00:00 | âge ticker : 149.1 s | durée : 149.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- BAT-EUR : 0.07972 € ; score 85.87/100 ; SURVEILLE ; seuil achat non atteint
- PLUME-EUR : 0.0149179 € ; score 84.99/100 ; SURVEILLE ; WICK_SETUP
- KAITO-EUR : 0.29723 € ; score 84.13/100 ; SURVEILLE ; seuil achat non atteint
- LTC-EUR : 59.985 € ; score 82.73/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- MAVIA-EUR : 0.029658 € ; score 80.39/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.002326 | +52.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.34931 | +28.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.11519 | +26.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RAY-EUR | 1.87668 | +18.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMU-EUR | 0.0019374 | +13.08 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| DBR-EUR | 0.018524 | +10.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOSO-EUR | 0.28859 | +10.65 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| CELR-EUR | 0.0028676 | +10.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.3502 | +7.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CVC-EUR | 0.026935 | +6.92 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1337 scans ; 572299 observations ; 689 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
