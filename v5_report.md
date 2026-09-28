# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T00:30:35.195964+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-28T00:30:02.471252+00:00 | âge ticker : 150.0 s | durée : 151.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- BABY-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- GMT-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PENGU-EUR : 0.009122 € | IGNITION | score 89.87/100 | entrée 6.90/10
  Entrée 0.0091395 € ; stop 0.0087171 € ; TP1 0.0099843 € ; TP2 0.0104067 € ; montant 226.18 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 3.697/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- EIGEN-EUR : 0.24727 € | IGNITION | score 87.17/100 | entrée 7.40/10
  Entrée 0.24802 € ; stop 0.23581 € ; TP1 0.27244 € ; TP2 0.28464 € ; montant 214.07 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 4.65/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RENDER-EUR : 1.8329 € ; score 95.26/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LPT-EUR : 1.5934 € ; score 92.63/100 ; SURVEILLE ; seuil achat non atteint
- ALGO-EUR : 0.105695 € ; score 90.59/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- CFG-EUR : 0.146706 € ; score 90.05/100 ; SURVEILLE ; seuil achat non atteint
- VIRTUAL-EUR : 0.74442 € ; score 89.40/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 261.844 | +88.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.29255 | +45.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRT-EUR | 0.031023 | +30.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006706 | +29.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| W-EUR | 0.013862 | +19.97 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.95601 | +19.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.0045324 | +17.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.07337 | +16.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMX-EUR | 0.16749 | +15.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| JASMY-EUR | 0.0047603 | +15.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1659 scans ; 709761 observations ; 1207 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
