# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T08:59:21.708216+00:00
État : OK | marchés EUR : 426 | V4 : 378 | données valides : 426
Récupération : 2026-09-21T08:58:29.236060+00:00 | âge ticker : 168.1 s | durée : 168.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- BTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : PORTFOLIO_LIMIT
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ETH-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : CORRELATED_OR_UNKNOWN_CORRELATION_REQUIRES_REVIEW
- QNT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, PORTFOLIO_LIMIT
- WLD-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : WICK_SETUP, PORTFOLIO_LIMIT
- SOL-EUR : 100.534 € | IGNITION | score 91.81/100 | entrée 7.95/10
  Entrée 100.533 € ; stop 96.721 € ; TP1 108.157 € ; TP2 111.969 € ; montant 250.00 € ; risque théorique 11.20 € ; R/R net 1.53.
  Chase risk : 8.563/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- XLM-EUR : 0.18004 € | IGNITION | score 88.10/100 | entrée 8.05/10
  Entrée 0.18002 € ; stop 0.17194 € ; TP1 0.19618 € ; TP2 0.20426 € ; montant 231.99 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 4.189/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- PENGU-EUR : 0.007192 € | IGNITION | score 87.86/100 | entrée 7.45/10
  Entrée 0.0071929 € ; stop 0.0069284 € ; TP1 0.0077219 € ; TP2 0.0079864 € ; montant 18.42 € ; risque théorique 0.80 € ; R/R net 1.52.
  Chase risk : 6.598/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- KAS-EUR : 0.035543 € ; score 93.38/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : 6.8086 € ; score 92.86/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : 0.38384 € ; score 92.48/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.07698 € ; score 91.99/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GRASS-EUR : 0.32092 € ; score 91.76/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.06043 | +81.99 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.0009193 | +51.25 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.033659 | +39.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.058094 | +35.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.2453 | +34.04 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| KMNO-EUR | 0.030505 | +30.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.5179 | +26.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.031 | +25.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.038372 | +23.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NEAR-EUR | 3.754 | +23.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1062 scans ; 455149 observations ; 332 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
