# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T20:12:21.548263+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-21T20:11:53.916639+00:00 | âge ticker : 147.8 s | durée : 148.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AKT-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- BCH-EUR : INSUFFICIENT_NET_RISK_REWARD
- BTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : 0.0079435 € | IGNITION | score 91.61/100 | entrée 7.80/10
  Entrée 0.0079487 € ; stop 0.0075975 € ; TP1 0.008651 € ; TP2 0.0090022 € ; montant 235.16 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 3.188/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- XLM-EUR : 0.18731 € | IGNITION | score 89.05/100 | entrée 8.05/10
  Entrée 0.18743 € ; stop 0.17974 € ; TP1 0.20281 € ; TP2 0.2105 € ; montant 250.00 € ; risque théorique 11.97 € ; R/R net 1.56.
  Chase risk : 2.234/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SOL-EUR : 103.355 € ; score 92.01/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SXT-EUR : 0.007832 € ; score 88.32/100 ; SURVEILLE ; seuil achat non atteint
- BTC-EUR : 75654 € ; score 87.78/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BRETT-EUR : 0.0051108 € ; score 87.77/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- CHZ-EUR : 0.013812 € ; score 86.34/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.01791 | +112.46 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.00166 | +112.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.053194 | +56.87 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AIOZ-EUR | 0.110216 | +39.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.045193 | +38.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.30519 | +35.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.001053 | +31.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008463 | +30.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.33574 | +24.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.319e-06 | +23.99 % | DETECTED_EARLY | NONE | NONE |

Historique : 1109 scans ; 475171 observations ; 404 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
