# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T01:18:52.736729+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-25T01:18:23.477271+00:00 | âge ticker : 154.7 s | durée : 155.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : EXTENDED_24H, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : 0.9184 € | IGNITION | score 92.61/100 | entrée 7.60/10
  Entrée 0.92011 € ; stop 0.88166 € ; TP1 0.99701 € ; TP2 1.03546 € ; montant 246.70 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 3.648/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- XLM-EUR : 0.19402 € | IGNITION | score 82.64/100 | entrée 7.55/10
  Entrée 0.19477 € ; stop 0.18776 € ; TP1 0.20878 € ; TP2 0.21579 € ; montant 250.00 € ; risque théorique 10.72 € ; R/R net 1.51.
  Chase risk : 3.66/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ADA-EUR : 0.22256 € ; score 91.01/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AEVO-EUR : 0.022491 € ; score 89.39/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- BCH-EUR : 298.9 € ; score 88.81/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.10046 € ; score 88.31/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : 11.8172 € ; score 88.25/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.060611 | +45.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XPL-EUR | 0.103004 | +31.51 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.46789 | +29.88 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 79.066 | +28.21 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.60809 | +24.10 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| DBR-EUR | 0.021887 | +23.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XAI-EUR | 0.0083705 | +20.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.036442 | +18.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DYM-EUR | 0.018681 | +18.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.19875 | +17.13 % | DETECTED_EARLY | NONE | NONE |

Historique : 1405 scans ; 601303 observations ; 790 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
