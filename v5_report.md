# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T20:00:57.580099+00:00
État : OK | marchés EUR : 426 | V4 : 403 | données valides : 426
Récupération : 2026-09-21T20:00:29.478703+00:00 | âge ticker : 153.5 s | durée : 154.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : INSUFFICIENT_NET_RISK_REWARD
- BTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- STX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : 0.0079389 € | IGNITION | score 93.53/100 | entrée 8.00/10
  Entrée 0.0079348 € ; stop 0.0075975 € ; TP1 0.0086094 € ; TP2 0.0089467 € ; montant 243.11 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 3.485/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- RAY-EUR : 1.59607 € | IGNITION | score 79.66/100 | entrée 7.15/10
  Entrée 1.59504 € ; stop 1.49655 € ; TP1 1.79202 € ; TP2 1.89051 € ; montant 175.10 € ; risque théorique 12.00 € ; R/R net 1.69.
  Chase risk : 4.041/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- XTZ-EUR : 0.30929 € ; score 91.37/100 ; SURVEILLE ; WICK_SETUP
- LUNA2-EUR : 0.047358 € ; score 89.11/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- BIGTIME-EUR : 0.00719 € ; score 88.47/100 ; SURVEILLE ; seuil achat non atteint
- BTC-EUR : 75537 € ; score 87.14/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.18434 € ; score 86.45/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017676 | +109.68 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0016007 | +107.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.0535 | +57.78 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.045701 | +40.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AIOZ-EUR | 0.109493 | +37.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.30582 | +36.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0010497 | +31.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.000835 | +28.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.3304 | +24.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.3293e-06 | +23.91 % | DETECTED_EARLY | NONE | NONE |

Historique : 1108 scans ; 474745 observations ; 404 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
