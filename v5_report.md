# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T09:54:48.265332+00:00
État : OK | marchés EUR : 426 | V4 : 381 | données valides : 426
Récupération : 2026-09-21T09:54:13.921757+00:00 | âge ticker : 157.8 s | durée : 158.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : BELOW_EXCHANGE_MINIMUM
- PUMP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- STX-EUR : 0.29086 € | IGNITION | score 84.58/100 | entrée 6.95/10
  Entrée 0.29003 € ; stop 0.27564 € ; TP1 0.31881 € ; TP2 0.3332 € ; montant 212.61 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 5.927/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- LINK-EUR : 11.301 € | IGNITION | score 82.11/100 | entrée 7.20/10
  Entrée 11.3021 € ; stop 10.826 € ; TP1 12.2542 € ; TP2 12.7303 € ; montant 245.01 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 5.124/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- INJ-EUR : 6.8869 € ; score 92.59/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUSHI-EUR : 0.22468 € ; score 90.68/100 ; SURVEILLE ; seuil achat non atteint
- SYRUP-EUR : 0.20449 € ; score 88.46/100 ; SURVEILLE ; WICK_SETUP
- MERL-EUR : 0.023789 € ; score 85.93/100 ; SURVEILLE ; seuil achat non atteint
- WAL-EUR : 0.029652 € ; score 85.90/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.056686 | +71.86 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.0009777 | +57.19 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PHA-EUR | 0.046367 | +48.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.060311 | +40.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.03043 | +31.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.24015 | +31.23 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.031066 | +27.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.031918 | +27.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VVV-EUR | 29.6274 | +23.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DRIFT-EUR | 0.015483 | +22.69 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 1066 scans ; 456853 observations ; 338 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
