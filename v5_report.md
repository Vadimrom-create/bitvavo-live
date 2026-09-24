# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T12:30:45.652725+00:00
État : OK | marchés EUR : 426 | V4 : 396 | données valides : 426
Récupération : 2026-09-24T12:30:11.268107+00:00 | âge ticker : 147.1 s | durée : 148.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : BELOW_EXCHANGE_MINIMUM
- QNT-EUR : 65.16 € | IGNITION | score 89.37/100 | entrée 7.30/10
  Entrée 65.323 € ; stop 62.049 € ; TP1 71.87 € ; TP2 75.144 € ; montant 210.73 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 5.939/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ONDO-EUR : 0.39991 € | IGNITION | score 84.34/100 | entrée 6.70/10
  Entrée 0.39934 € ; stop 0.36436 € ; TP1 0.46929 € ; TP2 0.50427 € ; montant 127.27 € ; risque théorique 12.00 € ; R/R net 1.78.
  Chase risk : 8.416/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ICP-EUR : 2.6159 € ; score 87.34/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- CVC-EUR : 0.027485 € ; score 86.75/100 ; SURVEILLE ; WICK_SETUP
- JUP-EUR : 0.25626 € ; score 85.96/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- CFG-EUR : 0.124982 € ; score 85.04/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LAPTOP-EUR : 0.06075 € ; score 84.98/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0021332 | +37.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.34946 | +25.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.10697 | +23.24 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARX-EUR | 0.21819 | +15.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.047056 | +13.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IMU-EUR | 0.00192 | +9.97 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CVC-EUR | 0.027485 | +9.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOSO-EUR | 0.28477 | +8.30 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| CNPY-EUR | 0.38726 | +7.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LTC-EUR | 58.027 | +6.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1355 scans ; 579967 observations ; 716 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
