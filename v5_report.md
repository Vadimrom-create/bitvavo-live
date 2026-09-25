# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T10:18:00.115961+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 427
Récupération : 2026-09-25T10:17:30.131515+00:00 | âge ticker : 155.7 s | durée : 156.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : 0.019273 € | IGNITION | score 90.62/100 | entrée 6.80/10
  Entrée 0.019313 € ; stop 0.018565 € ; TP1 0.020808 € ; TP2 0.021556 € ; montant 250.00 € ; risque théorique 11.40 € ; R/R net 1.54.
  Chase risk : 3.845/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- VET-EUR : 0.0081323 € ; score 93.27/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BONK-EUR : 3.2391e-06 € ; score 92.09/100 ; SURVEILLE ; seuil achat non atteint
- RAY-EUR : 1.82508 € ; score 91.01/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- A-EUR : 0.087423 € ; score 88.44/100 ; SURVEILLE ; seuil achat non atteint
- FRAX-EUR : 0.26454 € ; score 85.94/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.73735 | +45.83 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 87.295 | +40.00 % | DETECTED_EARLY | NONE | NONE |
| ONDO-EUR | 0.48701 | +31.51 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.100374 | +29.65 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.19446 | +27.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.052652 | +25.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FET-EUR | 0.20999 | +22.33 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.038493 | +21.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.086039 | +18.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CHIP-EUR | 0.043028 | +17.67 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1436 scans ; 614540 observations ; 827 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
