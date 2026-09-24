# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T12:07:50.386729+00:00
État : OK | marchés EUR : 426 | V4 : 396 | données valides : 426
Récupération : 2026-09-24T12:07:17.970026+00:00 | âge ticker : 145.8 s | durée : 147.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.39807 € | IGNITION | score 86.59/100 | entrée 6.80/10
  Entrée 0.39815 € ; stop 0.36598 € ; TP1 0.46248 € ; TP2 0.49465 € ; montant 137.12 € ; risque théorique 12.00 € ; R/R net 1.76.
  Chase risk : 0.883/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- JUP-EUR : 0.25505 € ; score 90.23/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- G-EUR : 0.0048942 € ; score 88.34/100 ; SURVEILLE ; seuil achat non atteint
- MOVR-EUR : 0.7745 € ; score 87.77/100 ; SURVEILLE ; seuil achat non atteint
- LAPTOP-EUR : 0.061 € ; score 85.05/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP, STABILITY_HOLD
- LTC-EUR : 57.828 € ; score 83.30/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0021546 | +39.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.111938 | +30.16 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| LSK-EUR | 0.34975 | +26.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.21667 | +15.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CVC-EUR | 0.028385 | +13.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IMU-EUR | 0.00198 | +13.40 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.045122 | +8.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOSO-EUR | 0.28577 | +8.68 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| CNPY-EUR | 0.38337 | +8.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LTC-EUR | 57.828 | +6.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1354 scans ; 579541 observations ; 715 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
