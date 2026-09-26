# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T07:51:32.136638+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-26T07:51:04.228255+00:00 | âge ticker : 158.3 s | durée : 160.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- AXS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- W-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XPL-EUR : 0.102481 € | IGNITION | score 81.87/100 | entrée 7.05/10
  Entrée 0.102528 € ; stop 0.097357 € ; TP1 0.112869 € ; TP2 0.11804 € ; montant 209.58 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 4.849/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RENDER-EUR : 1.7129 € ; score 93.34/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- W-EUR : 0.011029 € ; score 93.20/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : 0.0019224 € ; score 93.18/100 ; SURVEILLE ; seuil achat non atteint
- TIA-EUR : 0.43015 € ; score 92.35/100 ; SURVEILLE ; seuil achat non atteint
- ICP-EUR : 2.8256 € ; score 92.19/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016174 | +107.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.018939 | +64.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.24829 | +35.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.066708 | +33.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.0625 | +30.06 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ENA-EUR | 0.24141 | +24.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.77265 | +21.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0040342 | +17.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.038693 | +17.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CC-EUR | 0.12133 | +17.37 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1514 scans ; 647846 observations ; 958 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
