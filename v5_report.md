# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T21:23:31.028100+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-21T21:22:58.969779+00:00 | âge ticker : 152.4 s | durée : 153.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- BCH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : LOW_LIQUIDITY, WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.39516 € | IGNITION | score 92.73/100 | entrée 8.15/10
  Entrée 0.39502 € ; stop 0.38105 € ; TP1 0.42295 € ; TP2 0.43692 € ; montant 250.00 € ; risque théorique 10.56 € ; R/R net 1.50.
  Chase risk : 2.24/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- STX-EUR : 0.30009 € | IGNITION | score 86.21/100 | entrée 7.20/10
  Entrée 0.29965 € ; stop 0.28805 € ; TP1 0.32285 € ; TP2 0.33445 € ; montant 250.00 € ; risque théorique 11.39 € ; R/R net 1.54.
  Chase risk : 4.862/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RSR-EUR : 0.0014162 € ; score 88.03/100 ; SURVEILLE ; STABILITY_HOLD
- BABY-EUR : 0.010702 € ; score 84.49/100 ; SURVEILLE ; seuil achat non atteint
- ICP-EUR : 2.5918 € ; score 82.04/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BIGTIME-EUR : 0.007186 € ; score 79.88/100 ; SURVEILLE ; seuil achat non atteint
- ATH-EUR : 0.0048732 € ; score 79.17/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0017469 | +123.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.0168 | +99.38 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.052273 | +51.72 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AIOZ-EUR | 0.110315 | +39.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.31038 | +38.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.044064 | +36.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.001044 | +31.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008268 | +27.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.39226 | +26.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.255502 | +24.01 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1117 scans ; 478579 observations ; 405 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
