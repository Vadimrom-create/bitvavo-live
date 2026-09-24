# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T06:41:02.261869+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-24T06:40:31.434336+00:00 | âge ticker : 145.0 s | durée : 145.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HBAR-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD
- W-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZBT-EUR : 0.077493 € ; score 89.22/100 ; SURVEILLE ; seuil achat non atteint
- DEEP-EUR : 0.016718 € ; score 87.57/100 ; SURVEILLE ; seuil achat non atteint
- FORM-EUR : 0.2627 € ; score 86.71/100 ; SURVEILLE ; seuil achat non atteint
- HBAR-EUR : 0.080568 € ; score 85.64/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PLUME-EUR : 0.0144884 € ; score 85.56/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0023846 | +55.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.35004 | +27.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.112227 | +17.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RAY-EUR | 1.84767 | +16.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMU-EUR | 0.0019426 | +14.20 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOSO-EUR | 0.29374 | +12.73 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| DBR-EUR | 0.018551 | +11.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.3796 | +10.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CELR-EUR | 0.0027938 | +8.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VTHO-EUR | 0.00067903 | +7.83 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1335 scans ; 571447 observations ; 687 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
