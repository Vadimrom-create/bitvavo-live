# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T01:21:54.484517+00:00
État : OK | marchés EUR : 426 | V4 : 383 | données valides : 426
Récupération : 2026-09-21T01:21:23.620613+00:00 | âge ticker : 144.0 s | durée : 144.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- APT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETHFI-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PHA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PYTH-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : STABILITY_HOLD, PORTFOLIO_LIMIT
- SUI-EUR : STABILITY_HOLD, PORTFOLIO_LIMIT
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AERO-EUR : 0.59189 € | IGNITION | score 89.31/100 | entrée 6.90/10
  Entrée 0.59232 € ; stop 0.56841 € ; TP1 0.64013 € ; TP2 0.66404 € ; montant 250.00 € ; risque théorique 11.81 € ; R/R net 1.55.
  Chase risk : 4.279/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- FET-EUR : 0.15727 € | IGNITION | score 83.81/100 | entrée 7.85/10
  Entrée 0.15737 € ; stop 0.15154 € ; TP1 0.16903 € ; TP2 0.17486 € ; montant 250.00 € ; risque théorique 10.98 € ; R/R net 1.52.
  Chase risk : 3.742/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- XPL-EUR : 0.080418 € | IGNITION | score 82.53/100 | entrée 7.25/10
  Entrée 0.08019 € ; stop 0.077203 € ; TP1 0.086164 € ; TP2 0.089151 € ; montant 27.53 € ; risque théorique 1.21 € ; R/R net 1.52.
  Chase risk : 2.106/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LTC-EUR : 51.768 € ; score 88.00/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : 0.054493 € ; score 87.75/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FARTCOIN-EUR : 0.14841 € ; score 86.50/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BAND-EUR : 0.17909 € ; score 85.79/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- TAO-EUR : 234.52 € ; score 85.19/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.033593 | +47.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0008293 | +34.08 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.24124 | +30.74 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.50596 | +28.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.054708 | +23.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CFG-EUR | 0.130748 | +20.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.028906 | +19.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.7188 | +19.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| S-EUR | 0.034176 | +19.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 10.1923 | +18.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1036 scans ; 444073 observations ; 286 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
