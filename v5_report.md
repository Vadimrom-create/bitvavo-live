# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T00:53:49.279139+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-28T00:53:17.052215+00:00 | âge ticker : 157.4 s | durée : 158.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BABY-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : 0.24668 € | IGNITION | score 92.72/100 | entrée 7.35/10
  Entrée 0.24638 € ; stop 0.23584 € ; TP1 0.26746 € ; TP2 0.27799 € ; montant 241.79 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 2.402/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- PENGU-EUR : 0.0091467 € | IGNITION | score 80.49/100 | entrée 7.20/10
  Entrée 0.0091448 € ; stop 0.0087159 € ; TP1 0.0100025 € ; TP2 0.0104314 € ; montant 223.31 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 1.897/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RENDER-EUR : 1.815 € ; score 92.39/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MON-EUR : 0.025156 € ; score 90.59/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- HBAR-EUR : 0.084789 € ; score 87.87/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : 0.095481 € ; score 86.92/100 ; SURVEILLE ; WICK_SETUP
- DOGE-EUR : 0.085801 € ; score 86.03/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 241.297 | +74.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.29409 | +41.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006668 | +29.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.030501 | +27.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 1.0406 | +27.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.0046 | +19.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.074963 | +19.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IRYS-EUR | 0.017475 | +19.55 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| IMX-EUR | 0.16638 | +15.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.013635 | +14.73 % | DETECTED_EARLY | NONE | NONE |

Historique : 1660 scans ; 710188 observations ; 1209 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
