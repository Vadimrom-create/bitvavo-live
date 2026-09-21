# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T09:42:37.705624+00:00
État : OK | marchés EUR : 426 | V4 : 379 | données valides : 426
Récupération : 2026-09-21T09:42:10.970675+00:00 | âge ticker : 141.3 s | durée : 142.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, CORRELATED_OR_UNKNOWN_CORRELATION_REQUIRES_REVIEW
- ALGO-EUR : WICK_SETUP, BELOW_EXCHANGE_MINIMUM
- BNB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ETH-EUR : BELOW_EXCHANGE_MINIMUM
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : CORRELATED_OR_UNKNOWN_CORRELATION_REQUIRES_REVIEW
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PYTH-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SOL-EUR : WICK_SETUP, CORRELATED_OR_UNKNOWN_CORRELATION_REQUIRES_REVIEW
- WIF-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- LINK-EUR : 11.3998 € | IGNITION | score 88.91/100 | entrée 7.60/10
  Entrée 11.402 € ; stop 10.8294 € ; TP1 12.5471 € ; TP2 13.1197 € ; montant 210.37 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 4.026/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- EIGEN-EUR : 0.21263 € | IGNITION | score 85.70/100 | entrée 7.80/10
  Entrée 0.21175 € ; stop 0.20248 € ; TP1 0.23029 € ; TP2 0.23956 € ; montant 237.04 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 4.262/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ARX-EUR : 0.17391 € ; score 93.67/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- SENT-EUR : 0.016585 € ; score 92.96/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- INJ-EUR : 6.8868 € ; score 92.88/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : 0.1255 € ; score 92.77/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- HBAR-EUR : 0.077544 € ; score 91.61/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.056854 | +72.37 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.0009638 | +54.95 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PHA-EUR | 0.047186 | +50.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.059515 | +38.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.030639 | +30.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.23581 | +28.86 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.031541 | +28.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.031829 | +27.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.51356 | +24.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DRIFT-EUR | 0.015758 | +23.81 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 1065 scans ; 456427 observations ; 337 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
