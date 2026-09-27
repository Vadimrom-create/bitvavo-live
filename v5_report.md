# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T19:28:42.813011+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T19:28:13.966599+00:00 | âge ticker : 151.6 s | durée : 152.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AXS-EUR : INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TIA-EUR : INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.309 € | IGNITION | score 86.65/100 | entrée 7.15/10
  Entrée 0.30807 € ; stop 0.2955 € ; TP1 0.33321 € ; TP2 0.34578 € ; montant 250.00 € ; risque théorique 11.91 € ; R/R net 1.56.
  Chase risk : 5.855/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ARB-EUR : 0.20119 € | IGNITION | score 85.50/100 | entrée 7.45/10
  Entrée 0.20152 € ; stop 0.19399 € ; TP1 0.21658 € ; TP2 0.22411 € ; montant 250.00 € ; risque théorique 11.06 € ; R/R net 1.53.
  Chase risk : 3.587/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- DUSK-EUR : 0.080369 € ; score 93.27/100 ; SURVEILLE ; SPREAD_RISK
- DATAIP-EUR : 0.2056 € ; score 91.68/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.083432 € ; score 91.21/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : 0.107607 € ; score 90.67/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : 0.11422 € ; score 90.20/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 165.23 | +53.14 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.28458 | +45.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.96979 | +30.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.016433 | +29.27 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| INX-EUR | 0.006464 | +25.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.007306 | +22.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| W-EUR | 0.013851 | +20.67 % | DETECTED_EARLY | NONE | NONE |
| ARX-EUR | 0.24336 | +20.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.00698 | +16.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.027573 | +13.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1640 scans ; 701648 observations ; 1164 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
